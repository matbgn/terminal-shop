# Start documenting using docsify

---

1. Init npm repo and install docsify-cli or do it globally
   ```
      npm init
      npm i -D docsify-cli
   
   OR
   
      npm i docsify-cli -g
   ```
1. Init docs folder
   ```json
   docsify init ./docs
   ```
1. Add search support in `./docs/index.html` by adding following line before body's end
   ```html
   <script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
   ```