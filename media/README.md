# Central MESA media

36 original photographs and the SVG mark are served byte-for-byte from `https://media.pfxamd.com/pfxamd/concepts/mesa/`. Source originals remain in GitHub, alongside the older docs snapshot.

The workflow builds and checks fresh `dist` before publishing. It no longer uploads the docs folder containing source notes and archived local images. `publish_media.py` validates original hashes and R2 download evidence before rewriting generated media references and omitting generated local copies. The existing design, recipe data, CSS, JS, cooking/pantry interactions and optional font behavior are preserved.

Update the manifest and public HTTPS hash/size verification after uploading any new originals, before changing production links. No Cloudflare credentials are stored or needed in GitHub. The existing push-to-main workflow performs automatic publication, with no manual dispatch.
