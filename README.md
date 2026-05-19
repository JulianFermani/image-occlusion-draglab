<p align="center"><img src="screenshots/logo.png" width=381 height=224></p>

<h2 align="center">Image Occlusion DragLab for Anki</h2>

<p align="center">
<a title="Repository" href="https://github.com/JulianFermani/image-occlusion-draglab"><img src="https://img.shields.io/badge/GitHub-image--occlusion--draglab-brightgreen"></a>
<a title="License: GNU AGPLv3" href="https://github.com/JulianFermani/image-occlusion-draglab/blob/main/LICENSE"><img  src="https://img.shields.io/badge/license-GNU AGPLv3-green.svg"></a>
<br>
<a title="Buy me a coffee :)" href="https://ko-fi.com/X8X0L4YV"><img src="https://img.shields.io/badge/ko--fi-contribute-%23579ebd.svg"></a>
<a title="Support me on Patreon :D" href="https://www.patreon.com/bePatron?u=7522179"><img src="https://img.shields.io/badge/patreon-support-%23f96854.svg"></a>
<a title="Follow me on Twitter" href="https://twitter.com/intent/user?screen_name=glutanimate"><img src="https://img.shields.io/twitter/follow/glutanimate.svg"></a>
</p>

> Flashcards from images – the easy way

*Image Occlusion DragLab* is an add-on for the spaced repetition flashcard app [Anki](https://apps.ankiweb.net/) that allows you to create image-based cloze-deletions and interactive drag-and-drop exercises. It is based on Image Occlusion Enhanced and adds a drag-and-drop review mode for worksheets, diagrams, tables, and network exercises where one image contains multiple blanks to complete.

### Table of Contents <!-- omit in toc -->

<!-- MarkdownTOC levels="1,2,3" -->

- [Screenshots](#screenshots)
- [Installation](#installation)
- [Documentation](#documentation)
- [Drag and Drop Mode](#drag-and-drop-mode)
- [Building](#building)
- [Contributing](#contributing)
- [License and Credits](#license-and-credits)

<!-- /MarkdownTOC -->

### Screenshots

*Creating Cards With the Add-on:*

<img src="screenshots/screenshot-io-editor-1.png">
<img src="screenshots/screenshot-io-editor-2.png">

*Reviewing Generated Cards:*

<img src="screenshots/screenshot-io-reviewer.png">

### Installation

#### Manual installation <!-- omit in toc -->

1. Make sure you have the [latest version](https://apps.ankiweb.net/#download) of Anki 2.1 installed. Earlier releases (e.g. found in various Linux distros) do not support `.ankiaddon` packages.
2. Download the latest `.ankiaddon` package from the [releases tab](https://github.com/JulianFermani/image-occlusion-draglab/releases) once a packaged release is available.
3. From Anki's main window, head to *Tools* → *Add-ons*
4. Drag-and-drop the `.ankiaddon` package onto the add-ons list
5. Restart Anki

### Documentation

The original Image Occlusion Enhanced documentation is available in the [Wiki](https://github.com/Glutanimate/image-occlusion-enhanced/wiki) and a [series of video tutorials on YouTube](https://www.youtube.com/playlist?list=PL3MozITKTz5YFHDGB19ypxcYfJ1ITk_6o). The drag-and-drop workflow added by this fork is documented below.

### Drag and Drop Mode

This fork includes a drag-and-drop card type designed for images with several blanks and a shared answer bank. It is useful for exercises such as completing labels in a diagram, filling table cells inside an image, or placing IP/MAC addresses in a network worksheet.

#### What it creates

- One Anki card per image.
- Multiple drop targets inside that image.
- A randomized list of draggable options below the image.
- A `Comprobar` button that marks answers as correct, incorrect, or empty.
- A back side that shows all correct answers in their positions.

#### How to create a drag-and-drop card

1. Open Image Occlusion DragLab from Anki's editor as usual.
2. Select or paste the image you want to turn into an exercise.
3. Draw one rectangle over each blank area that the user must complete.
4. Open the `Fields` tab.
5. In `Drag Options`, write one answer per line.
6. Keep the answer order aligned with the rectangle creation order: the first line belongs to the first rectangle, the second line to the second rectangle, and so on.
7. Select the destination deck in the editor window.
8. Click `Drag & Drop`.

Example `Drag Options` content:

```text
10.0.0.2
10.0.0.3
78:84:3c:ca:11:32
4c:0f:6e:d4:32:27
98:86:33:ba:15:33
10.0.0.254
```

#### Reviewing drag-and-drop cards

- Drag any option from the answer bank into any rectangle.
- Dropping an option into an occupied rectangle replaces the previous option.
- Options are shuffled every time the card is rendered, so the user cannot rely on the original creation order.
- Press `Comprobar` to check the current placement.
- Green means correct, red means incorrect, and yellow means empty.
- After checking, answers can still be moved and checked again.
- Use Anki's normal grading buttons (`Again`, `Hard`, `Good`, `Easy`) based on the result.

#### Best practices

- Use rectangles for blanks whenever possible. Rectangles are the most reliable shape for this mode.
- Draw the rectangles in the same order as the answer list you will enter in `Drag Options`.
- Make each rectangle slightly larger than the answer text area so the option is easy to drop.
- Use short labels. Long labels can overflow small blanks.
- If you need to edit the answer mapping, recreate the card or edit the hidden `Drag Data` field carefully.

#### Current limitations

- The add-on does not automatically read the text hidden under a rectangle. You must provide the answers manually in `Drag Options`.
- The validation is visual inside the card. It does not automatically press Anki's grading buttons.
- The mode is optimized for desktop Anki. Touch/mobile behavior may vary depending on the WebView used by Anki.
- Simple shapes are supported for target extraction: rectangles, circles, ellipses, lines, polygons, and simple groups. Rectangles are recommended.

### Building

With [Anki add-on builder](https://github.com/glutanimate/anki-addon-builder/) installed:

    git clone https://github.com/JulianFermani/image-occlusion-draglab.git
    cd image-occlusion-draglab
    aab build

For more information on the build process please refer to [`aab`'s documentation](https://github.com/glutanimate/anki-addon-builder/#usage).

### Contributing

Contributions are welcome! Please review the [contribution guidelines](./CONTRIBUTING.md) on how to:

- Report issues
- File pull requests
- Support the project as a non-developer

### License and Credits

*Image Occlusion DragLab* is maintained by [JulianFermani](https://github.com/JulianFermani) and is based on *Image Occlusion Enhanced*.

*Image Occlusion Enhanced* is

*Copyright © 2012-2015 [Tiago Barroso](https://github.com/tmbb)*

*Copyright © 2013 [Steve AW](https://github.com/steveaw)*

*Copyright © 2016-2022 [Aristotelis P.](https://glutanimate.com/) (Glutanimate)*

With code contributions from: Damien Elmes, Kyle Mills, James Kraus, Matt Restko

Drag-and-drop mode and this fork are maintained by [JulianFermani](https://github.com/JulianFermani).

-----

*Image Occlusion Enhanced* is based on [Image Occlusion 2.0](https://github.com/tmbb/image-occlusion-2) by Tiago Barroso and [Simple Picture Occlusion](https://github.com/steveaw/anki_addons) by Steve AW. All credit for the original add-ons goes to their respective authors. *Image Occlusion Enhanced* would not exist without their work.

I would also like to extend my heartfelt thanks to everyone who has helped with testing, provided suggestions, or contributed in any other way.

*Image Occlusion Enhanced* ships with the following third-party open-source software:

- [SVG Edit](https://github.com/SVG-Edit/svgedit) 2.6. Copyright (c) 2009-2012 by SVG-edit authors. Licensed under the MIT license.

- [Python Imaging Library](http://www.pythonware.com/products/pil/) (PIL) 1.1.7. Copyright (c) 1997-2011 by Secret Labs AB, Copyright (c) 1995-2011 by Fredrik Lundh. Licensed under the [PIL license](http://www.pythonware.com/products/pil/license.htm)

- [imagesize.py](https://github.com/shibukawa/imagesize_py) v0.7.1. Copyright (c) 2016 Yoshiki Shibukawa. Licensed under the MIT license.

Image Occlusion DragLab is free and open-source software. The add-on code that runs within Anki is released under the GNU AGPLv3 license, extended by a number of additional terms. For more information please see the [LICENSE](https://github.com/JulianFermani/image-occlusion-draglab/blob/main/LICENSE) file that accompanied this program.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.

----
<b>
<div align="center">The continued development of this add-on is made possible <br>thanks to my <a href="https://www.patreon.com/glutanimate">Patreon</a> and <a href="https://ko-fi.com/X8X0L4YV">Ko-Fi</a> supporters.
<br>You guys rock ❤️ !</div>
</b>
