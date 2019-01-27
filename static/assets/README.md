# App assets

Assets are static files that belong to the app like a logo or an icon or a 
favicon. These files go here. Much like the branding folder in the root brands 
the entire site, this assets folder brands your app.

## Instructions

- **Follow the naming convention specified.** Omniport is not sentient and will 
not locate your images if not named and placed according to the pattern. To
omit an asset, leave out the file.
- **Follow the size and aspect ratio guidelines.** This is so that the assets 
integrate harmoniously with the rest of the portal. As feature packed as 
Omniport is, it is not free of assumptions.
- **Follow the file format specification.** As a rule of thumb prefer `.svg`
or `.ico` when the image needs to scale up or down respectively. Preferred file
formats are given, best stick to them.
- **Customizing assets is optional.** All applications come with their assets
and there is no real need to replace them other than a fierce desire arising
within your hearts.

## Image specifications

File name      | Aspect ratio     | Height in use     | Formats
---------------|------------------|------------------:|-----------------------:
`favicon.ico`  | square           | 16, 32, 48 px     | multisize `.ico` only
`icon.xxx`     | square           | 2.0em _(~28px)_   | `.svg`, `.png`, `.jpg`
`logo.xxx`     | square           | 3.5em _(~49px)_   | `.svg`, `.png`, `.jpg`

All images should be provided in 2x size if not supplying in the `.svg` format
to ensure that they work well on HiDPI displays.

For best results, use [this site](https://realfavicongenerator.net/) to generate
your favicon.ico files.

## Assets

The default branding imagery has been designed by IMG designers and is bundled 
with the application. However, if you wish, you may replace them with your own.
    
Ensure that you provide all the required images. Omniport will not handle 
missing images on its own.