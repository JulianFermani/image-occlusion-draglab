# -*- coding: utf-8 -*-

# Image Occlusion Enhanced Add-on for Anki
#
# Copyright (C) 2016-2020  Aristotelis P. <https://glutanimate.com/>
# Copyright (C) 2012-2015  Tiago Barroso <tmbb@campus.ul.pt>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

"""
Handles the IO note type and card template
"""

from .config import *

# DEFAULT CARD TEMPLATES

iocard_front = """\
{{#%(src_img)s}}
{{#%(drag_data)s}}
<div id="io-header">{{%(header)s}}</div>
<div id="io-dnd" class="io-dnd-card">
  <div id="io-dnd-stage" class="io-dnd-stage">
    {{%(src_img)s}}
  </div>
  <div id="io-dnd-options" class="io-dnd-options" aria-label="Drag options"></div>
</div>
<div id="io-footer">{{%(footer)s}}</div>
<script id="io-dnd-data" type="application/json">{{%(drag_data)s}}</script>
<script>setTimeout(function(){ if (globalThis.imageOcclusion) imageOcclusion.initDragAndDrop(); }, 0);</script>
{{/%(drag_data)s}}
{{^%(drag_data)s}}
<div id="io-header">{{%(header)s}}</div>
<div id="io-wrapper">
  <div id="io-overlay">{{%(que)s}}</div>
  <div id="io-original">{{%(src_img)s}}</div>
</div>
<div id="io-footer">{{%(footer)s}}</div>

<script>
// Prevent original image from loading before mask
aFade = 50, qFade = 0;
var mask = document.querySelector('#io-overlay>img');
function loaded() {
    var original = document.querySelector('#io-original');
    original.style.visibility = "visible";
}
if (mask === null || mask.complete) {
    loaded();
} else {
    mask.addEventListener('load', loaded);
}
</script>
{{/%(drag_data)s}}
{{/%(src_img)s}}
""" % {
    "que": IO_FLDS["qm"],
    "ans": IO_FLDS["am"],
    "svg": IO_FLDS["om"],
    "src_img": IO_FLDS["im"],
    "header": IO_FLDS["hd"],
    "footer": IO_FLDS["ft"],
    "remarks": IO_FLDS["rk"],
    "sources": IO_FLDS["sc"],
    "extraone": IO_FLDS["e1"],
    "extratwo": IO_FLDS["e2"],
    "drag_data": IO_FLDS["dd"],
}

iocard_back = """\
{{#%(src_img)s}}
{{#%(drag_data)s}}
<div id="io-header">{{%(header)s}}</div>
<div id="io-dnd" class="io-dnd-card io-dnd-answer">
  <div id="io-dnd-stage" class="io-dnd-stage">
    {{%(src_img)s}}
  </div>
</div>
{{#%(footer)s}}<div id="io-footer">{{%(footer)s}}</div>{{/%(footer)s}}
<script id="io-dnd-data" type="application/json">{{%(drag_data)s}}</script>
<script>setTimeout(function(){ if (globalThis.imageOcclusion) imageOcclusion.initDragAndDrop(); }, 0);</script>
{{/%(drag_data)s}}
{{^%(drag_data)s}}
<div id="io-header">{{%(header)s}}</div>
<div id="io-wrapper">
  <div id="io-overlay">{{%(ans)s}}</div>
  <div id="io-original">{{%(src_img)s}}</div>
</div>
{{#%(footer)s}}<div id="io-footer">{{%(footer)s}}</div>{{/%(footer)s}}
<button id="io-revl-btn" onclick="toggle();">Toggle Masks</button>
<div id="io-extra-wrapper">
  <div id="io-extra">
    {{#%(remarks)s}}
      <div class="io-extra-entry">
        <div class="io-field-descr">%(remarks)s</div>{{%(remarks)s}}
      </div>
    {{/%(remarks)s}}
    {{#%(sources)s}}
      <div class="io-extra-entry">
        <div class="io-field-descr">%(sources)s</div>{{%(sources)s}}
      </div>
    {{/%(sources)s}}
    {{#%(extraone)s}}
      <div class="io-extra-entry">
        <div class="io-field-descr">%(extraone)s</div>{{%(extraone)s}}
      </div>
    {{/%(extraone)s}}
    {{#%(extratwo)s}}
      <div class="io-extra-entry">
        <div class="io-field-descr">%(extratwo)s</div>{{%(extratwo)s}}
      </div>
    {{/%(extratwo)s}}
  </div>
</div>

<script>
// Toggle answer mask on clicking the image
var toggle = function() {
  var amask = document.getElementById('io-overlay');
  if (amask.style.display === 'block' || amask.style.display === '')
    amask.style.display = 'none';
  else
    amask.style.display = 'block'
}

// Prevent original image from loading before mask
aFade = 50, qFade = 0;
var mask = document.querySelector('#io-overlay>img');
function loaded() {
    var original = document.querySelector('#io-original');
    original.style.visibility = "visible";
}
if (mask === null || mask.complete) {
    loaded();
} else {
    mask.addEventListener('load', loaded);
}
</script>
{{/%(drag_data)s}}
{{/%(src_img)s}}
""" % {
    "que": IO_FLDS["qm"],
    "ans": IO_FLDS["am"],
    "svg": IO_FLDS["om"],
    "src_img": IO_FLDS["im"],
    "header": IO_FLDS["hd"],
    "footer": IO_FLDS["ft"],
    "remarks": IO_FLDS["rk"],
    "sources": IO_FLDS["sc"],
    "extraone": IO_FLDS["e1"],
    "extratwo": IO_FLDS["e2"],
    "drag_data": IO_FLDS["dd"],
}

iocard_css = """\
/* GENERAL CARD STYLE */
.card {
  font-family: "Helvetica LT Std", Helvetica, Arial, Sans;
  font-size: 150%;
  text-align: center;
  color: black;
  background-color: white;
}

/* OCCLUSION CSS START - don't edit this */
#io-overlay {
  position:absolute;
  top:0;
  width:100%;
  z-index:3
}

#io-original {
  position:relative;
  top:0;
  width:100%;
  z-index:2;
  visibility: hidden;
}

#io-wrapper {
  position:relative;
  width: 100%;
}
/* OCCLUSION CSS END */

/* OTHER STYLES */
#io-header{
  font-size: 1.1em;
  margin-bottom: 0.2em;
}

#io-footer{
  max-width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 0.8em;
  font-style: italic;
}

#io-extra-wrapper{
  /* the wrapper is needed to center the
  left-aligned blocks below it */
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 0.5em;
}

#io-extra{
  text-align:center;
  display: inline-block;
}

.io-extra-entry{
  margin-top: 0.8em;
  font-size: 0.9em;
  text-align:left;
}

.io-field-descr{
  margin-bottom: 0.2em;
  font-weight: bold;
  font-size: 1em;
}

#io-revl-btn {
  font-size: 0.5em;
}

/* DRAG AND DROP CARDS */
.io-dnd-stage {
  position: relative;
  display: inline-block;
  max-width: 100%;
}

.io-dnd-stage > img {
  display: block;
  max-width: 100%;
  height: auto;
}

.io-dnd-target {
  position: absolute;
  box-sizing: border-box;
  border: 2px solid #444;
  background: #fff;
  min-width: 3em;
  min-height: 1.5em;
  display: flex;
  align-items: center;
  justify-content: center;
}

.io-dnd-target.io-dnd-over {
  outline: 3px solid #5aa7ff;
}

.io-dnd-options {
  margin-top: 0.75em;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.45em;
}

.io-dnd-option {
  cursor: grab;
  user-select: none;
  border: 2px solid #555;
  background: white;
  padding: 0.25em 0.7em;
  min-width: 5em;
  font-size: 0.85em;
  touch-action: none;
  z-index: 10;
}

.io-dnd-option:active {
  cursor: grabbing;
}

.io-dnd-option.io-dnd-dragging {
  position: fixed;
  left: 0;
  top: 0;
  pointer-events: none;
  opacity: 0.96;
  z-index: 9999;
}

.io-dnd-answer-label {
  padding: 0.15em 0.45em;
  background: rgba(255, 255, 255, 0.92);
  font-size: 0.8em;
}

/* ADJUSTMENTS FOR MOBILE DEVICES */

.mobile .card, .mobile #content {
  font-size: 120%;
  margin: 0;
}

.mobile #io-extra-wrapper {
  width: 95%;
}

.mobile #io-revl-btn {
  font-size: 0.8em;
}
"""

# INCREMENTAL UPDATES

html_overlay_onload = """\
<script>
// Prevent original image from loading before mask
aFade = 50, qFade = 0;
var mask = document.querySelector('#io-overlay>img');
function loaded() {
    var original = document.querySelector('#io-original');
    original.style.visibility = "visible";
}
if (mask.complete) {
    loaded();
} else {
    mask.addEventListener('load', loaded);
}
</script>\
"""

css_original_hide = """\
/* Anki 2.1 additions */
#io-original {
   visibility: hidden;
}\
"""

# List structure:
# (<version addition was introduced in>,
# (<qfmt_addition>, <afmt_addition>, <css_addition>))
# versions need to be ordered by semantic versioning
additions_by_version = [
    (1.30, (html_overlay_onload, html_overlay_onload, css_original_hide)),
]


def add_io_model(col):
    models = col.models
    io_model = models.new(IO_MODEL_NAME)
    # Add fields:
    for i in IO_FLDS_IDS:
        fld = models.newField(IO_FLDS[i])
        if i == "note_id":
            fld["size"] = 0
        models.addField(io_model, fld)
    # Add template
    template = models.newTemplate(IO_CARD_NAME)
    template["qfmt"] = iocard_front
    template["afmt"] = iocard_back
    io_model["css"] = iocard_css
    io_model["sortf"] = 1  # set sortfield to header
    models.addTemplate(io_model, template)
    models.add(io_model)
    return io_model


def ensure_io_fields(col, io_model):
    models = col.models
    field_names = models.fieldNames(io_model)
    for i in IO_FLDS_IDS:
        field_name = IO_FLDS[i]
        if field_name in field_names:
            continue
        fld = models.newField(field_name)
        models.addField(io_model, fld)
        field_names.append(field_name)


def reset_template(col):
    print("Resetting IO Enhanced card template to defaults")
    io_model = col.models.byName(IO_MODEL_NAME)
    template = io_model["tmpls"][0]
    template["qfmt"] = iocard_front
    template["afmt"] = iocard_back
    io_model["css"] = iocard_css
    col.models.save()
    return io_model


def update_template(col, old_version):
    print("Updating IO Enhanced card template")

    additions = [[], [], []]

    for version, components in additions_by_version:
        if old_version >= version:
            continue
        for lst, addition in zip(additions, components):
            lst.append(addition)

    io_model = col.models.byName(IO_MODEL_NAME)

    if not io_model:
        return add_io_model(col)

    ensure_io_fields(col, io_model)

    template = io_model["tmpls"][0]
    if old_version < 1.33:
        template["qfmt"] = iocard_front
        template["afmt"] = iocard_back
        io_model["css"] = iocard_css
    else:
        template["qfmt"] += "\n".join(additions[0])
        template["afmt"] += "\n".join(additions[1])
        io_model["css"] += "\n".join(additions[2])
    col.models.save()
    return io_model
