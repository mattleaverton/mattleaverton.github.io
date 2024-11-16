Title: ES Modules in Vanilla JS
Modified: 2023-09-16 14:42
Date: 2023-09-16 14:42
Category: Writing
Tags:
Slug:
Authors: Matt Leaverton
Summary:
Status: published

I "learned" Javascript back in the good old days when jquery was the cutting edge, so it's no surprise that I find myself drawn to [Vanilla JS](http://vanilla-js.com/) as my weapon of choice.

Javascript build systems make me sad (a discussion for another time), but so many new and existing javascript libraries target build systems and cannot be used in Vanilla JS, or so I thought.

It turns out that it's just as simple as adding `type="module"` to the script tag, with no arcane build configurations required.

```javascript
<script type="module" src="main.js"></script>
```
