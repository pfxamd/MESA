$ErrorActionPreference='Stop'
$repo='https://github.com/pfxamd/MESA.git'
$root=Split-Path -Parent $MyInvocation.MyCommand.Path
foreach($name in @('git','python')) {
  if(-not (Get-Command $name -ErrorAction SilentlyContinue)) { throw "$name is required. Install it and try again." }
}
Push-Location $root
try { & python build.py; if($LASTEXITCODE -ne 0){throw 'Site build failed'}; & python tests/check_site.py; if($LASTEXITCODE -ne 0){throw 'Local checks failed'} } finally {Pop-Location}
$temp=Join-Path ([IO.Path]::GetTempPath()) ('mesa-upload-'+[guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Force -Path $temp | Out-Null
try {
  & git clone --branch main --single-branch $repo $temp
  if($LASTEXITCODE -ne 0){throw 'Could not clone repository. Check GitHub login.'}
  $oldBrief=Join-Path $temp 'README.md'
  $archiveBrief=Join-Path $temp 'planning\original-production-brief.md'
  if((Test-Path $oldBrief) -and -not(Test-Path $archiveBrief)){
    New-Item -ItemType Directory -Force -Path (Split-Path $archiveBrief) | Out-Null
    Copy-Item $oldBrief $archiveBrief
  }
  foreach($folder in @('assets','content','data','public','docs','tests')){
    $target=Join-Path $temp $folder
    New-Item -ItemType Directory -Force -Path $target | Out-Null
    Copy-Item -Path (Join-Path (Join-Path $root $folder) '*') -Destination $target -Recurse -Force
  }
  foreach($file in @('README.md','.gitignore','build.py','create_content.py','serve.py','preview.bat','upload-to-github.ps1','upload-to-github.bat')){
    Copy-Item -Path (Join-Path $root $file) -Destination (Join-Path $temp $file) -Force
  }
  Push-Location $temp
  try {
    & git add -A
    & git diff --cached --quiet
    if($LASTEXITCODE -eq 0){Write-Host 'Nothing changed.';return}
    & git commit -m 'feat: build MESA editorial culinary website'
    if($LASTEXITCODE -ne 0){throw 'Commit failed. Configure your Git username and email.'}
    & git push origin main
    if($LASTEXITCODE -ne 0){throw 'Push failed. Check GitHub authentication or branch changes.'}
    & git log -1 --oneline
    Write-Host 'Source and prebuilt pages uploaded to GitHub. No Pages publication settings were changed.'
  } finally {Pop-Location}
} finally {
  if(Test-Path $temp){Remove-Item $temp -Recurse -Force -ErrorAction SilentlyContinue}
}
