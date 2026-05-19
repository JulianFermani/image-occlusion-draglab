/* 
Image Occlusion Enhanced Add-on for Anki

Copyright (C) 2016-2022  Aristotelis P. <https://glutanimate.com/>
Copyright (C) 2012-2015  Tiago Barroso <tmbb@campus.ul.pt>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version, with the additions
listed at the end of the license file that accompanied this program.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

NOTE: This program is subject to certain additional terms pursuant to
Section 7 of the GNU Affero General Public License.  You should have
received a copy of these additional terms immediately following the
terms and conditions of the GNU Affero General Public License that
accompanied this program.

If not, please request a copy through one of the means of contact
listed here: <https://glutanimate.com/contact/>.

Any modifications to this file must keep this entire header intact.
*/

class ImageOcclusionReviewerAdapter {
  toggleMasks() {
    const ioButton = document.getElementById("io-revl-btn");
    if (ioButton) {
      ioButton.click();
    }
  }

  initDragAndDrop() {
    initImageOcclusionDragAndDrop();
  }
}

globalThis.imageOcclusion = new ImageOcclusionReviewerAdapter();

function initImageOcclusionDragAndDrop() {
  const dataElement = document.getElementById("io-dnd-data");
  const stage = document.getElementById("io-dnd-stage");
  if (!dataElement || !stage || stage.dataset.ioDndReady === "1") {
    return;
  }

  ensureDragAndDropStyles();

  let data;
  try {
    data = JSON.parse(dataElement.textContent);
  } catch (error) {
    console.error("Invalid image occlusion drag data", error);
    return;
  }

  const targets = Array.isArray(data.targets) ? data.targets : [];
  const options = document.getElementById("io-dnd-options");
  const isAnswer = document.querySelector(".io-dnd-answer") !== null;
  stage.dataset.ioDndReady = "1";

  const targetElements = targets.map((target) => {
    const element = document.createElement("div");
    element.className = "io-dnd-target";
    element.dataset.targetId = target.id;
    element.dataset.correctLabel = target.label;
    element.style.left = `${target.x}%`;
    element.style.top = `${target.y}%`;
    element.style.width = `${target.width}%`;
    element.style.height = `${target.height}%`;
    element.style.setProperty("background", "#fff", "important");
    element.style.setProperty("opacity", "1", "important");
    stage.appendChild(element);

    if (isAnswer) {
      const label = document.createElement("div");
      label.className = "io-dnd-answer-label";
      label.textContent = target.label;
      label.style.setProperty("background", "#fff", "important");
      label.style.setProperty("opacity", "1", "important");
      element.appendChild(label);
    }

    return element;
  });

  if (isAnswer || !options) {
    return;
  }

  let dragged = null;
  let sourceParent = null;
  let dragOffsetX = 0;
  let dragOffsetY = 0;
  const controls = document.createElement("div");
  const checkButton = document.createElement("button");
  const result = document.createElement("div");

  controls.className = "io-dnd-controls";
  checkButton.className = "io-dnd-check";
  checkButton.type = "button";
  checkButton.textContent = "Comprobar";
  result.className = "io-dnd-result";
  controls.appendChild(checkButton);
  controls.appendChild(result);
  options.insertAdjacentElement("afterend", controls);
  checkButton.addEventListener("click", checkAnswers);

  function makeOption(target) {
    const option = document.createElement("div");
    option.className = "io-dnd-option";
    option.draggable = false;
    option.dataset.label = target.label;
    option.textContent = target.label;
    option.style.setProperty("background", "#fff", "important");
    option.style.setProperty("opacity", "1", "important");
    option.addEventListener("pointerdown", onPointerDown);
    return option;
  }

  function onPointerDown(event) {
    if (event.button !== undefined && event.button !== 0) {
      return;
    }

    event.preventDefault();
    dragged = event.currentTarget;
    sourceParent = dragged.parentElement;
    const rect = dragged.getBoundingClientRect();
    dragOffsetX = event.clientX - rect.left;
    dragOffsetY = event.clientY - rect.top;
    dragged.style.width = `${rect.width}px`;
    dragged.style.height = `${rect.height}px`;
    dragged.style.position = "fixed";
    dragged.style.left = "0";
    dragged.style.top = "0";
    dragged.style.pointerEvents = "none";
    dragged.style.zIndex = "9999";
    dragged.style.visibility = "visible";
    dragged.style.setProperty("background", "#fff", "important");
    dragged.style.setProperty("opacity", "1", "important");
    dragged.classList.add("io-dnd-dragging");
    document.body.appendChild(dragged);
    moveDragged(event.clientX, event.clientY);

    document.addEventListener("pointermove", onPointerMove);
    document.addEventListener("pointerup", onPointerUp, { once: true });
  }

  function onPointerMove(event) {
    if (!dragged) {
      return;
    }

    event.preventDefault();
    moveDragged(event.clientX, event.clientY);
    clearTargetHighlights();

    const dropTarget = getDropTarget(event.clientX, event.clientY);
    if (dropTarget && dropTarget.classList.contains("io-dnd-target")) {
      dropTarget.classList.add("io-dnd-over");
    }
  }

  function onPointerUp(event) {
    document.removeEventListener("pointermove", onPointerMove);
    clearTargetHighlights();

    if (!dragged) {
      return;
    }

    const dropTarget = getDropTarget(event.clientX, event.clientY);
    finishDrag(dropTarget);
  }

  function moveDragged(clientX, clientY) {
    dragged.style.transform = `translate(${clientX - dragOffsetX}px, ${
      clientY - dragOffsetY
    }px)`;
  }

  function getDropTarget(clientX, clientY) {
    const element = document.elementFromPoint(clientX, clientY);
    if (!element) {
      return null;
    }
    return element.closest(".io-dnd-target, .io-dnd-options");
  }

  function finishDrag(dropTarget) {
    dragged.classList.remove("io-dnd-dragging");
    dragged.style.width = "";
    dragged.style.height = "";
    dragged.style.position = "";
    dragged.style.left = "";
    dragged.style.top = "";
    dragged.style.pointerEvents = "";
    dragged.style.zIndex = "";
    dragged.style.transform = "";

    if (dropTarget && dropTarget.classList.contains("io-dnd-target")) {
      moveOption(dropTarget);
    } else if (dropTarget && dropTarget.classList.contains("io-dnd-options")) {
      options.appendChild(dragged);
    } else if (sourceParent) {
      sourceParent.appendChild(dragged);
    }

    clearValidation();

    dragged = null;
    sourceParent = null;
  }

  function clearTargetHighlights() {
    targetElements.forEach((target) => target.classList.remove("io-dnd-over"));
  }

  function clearValidation() {
    targetElements.forEach((target) => {
      target.classList.remove(
        "io-dnd-correct",
        "io-dnd-incorrect",
        "io-dnd-empty"
      );
    });
    result.textContent = "";
  }

  function checkAnswers() {
    let correct = 0;

    targetElements.forEach((target) => {
      target.classList.remove(
        "io-dnd-correct",
        "io-dnd-incorrect",
        "io-dnd-empty"
      );

      const option = target.querySelector(".io-dnd-option");
      if (!option) {
        target.classList.add("io-dnd-empty");
        return;
      }

      if (option.dataset.label === target.dataset.correctLabel) {
        target.classList.add("io-dnd-correct");
        correct += 1;
      } else {
        target.classList.add("io-dnd-incorrect");
      }
    });

    result.textContent = `${correct} / ${targetElements.length} correctas`;
    result.classList.toggle("io-dnd-result-ok", correct === targetElements.length);
  }

  function moveOption(target) {
    if (!dragged) {
      return;
    }

    const replaced = target.querySelector(".io-dnd-option");
    target.appendChild(dragged);

    if (!replaced) {
      return;
    }

    if (sourceParent && sourceParent.classList.contains("io-dnd-target")) {
      sourceParent.appendChild(replaced);
    } else {
      options.appendChild(replaced);
    }
  }

  shuffle(targets).forEach((target) => options.appendChild(makeOption(target)));
}

function shuffle(items) {
  const shuffled = [...items];
  for (let i = shuffled.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
}

function ensureDragAndDropStyles() {
  if (document.getElementById("io-dnd-runtime-style")) {
    return;
  }

  const style = document.createElement("style");
  style.id = "io-dnd-runtime-style";
  style.textContent = `
.io-dnd-target {
  background: #fff !important;
  opacity: 1 !important;
}
.io-dnd-target.io-dnd-correct {
  border-color: #1f8f3a !important;
  box-shadow: 0 0 0 3px rgba(31, 143, 58, 0.35) !important;
}
.io-dnd-target.io-dnd-incorrect {
  border-color: #c93838 !important;
  box-shadow: 0 0 0 3px rgba(201, 56, 56, 0.35) !important;
}
.io-dnd-target.io-dnd-empty {
  border-color: #c58b00 !important;
  box-shadow: 0 0 0 3px rgba(197, 139, 0, 0.35) !important;
}
.io-dnd-option {
  background: #fff !important;
  opacity: 1 !important;
  touch-action: none !important;
}
.io-dnd-option.io-dnd-dragging {
  position: fixed !important;
  pointer-events: none !important;
  visibility: visible !important;
  opacity: 1 !important;
  z-index: 9999 !important;
}
.io-dnd-answer-label {
  background: #fff !important;
  opacity: 1 !important;
}
.io-dnd-controls {
  margin-top: 0.7em !important;
  text-align: center !important;
}
.io-dnd-check {
  cursor: pointer !important;
  border: 2px solid #444 !important;
  background: #fff !important;
  color: #000 !important;
  padding: 0.3em 0.8em !important;
  font-size: 0.75em !important;
}
.io-dnd-result {
  margin-top: 0.35em !important;
  font-size: 0.75em !important;
  font-weight: bold !important;
}
.io-dnd-result-ok {
  color: #1f8f3a !important;
}`;
  document.head.appendChild(style);
}

document.addEventListener("DOMContentLoaded", initImageOcclusionDragAndDrop);
setTimeout(initImageOcclusionDragAndDrop, 0);

new MutationObserver(initImageOcclusionDragAndDrop).observe(document.documentElement, {
  childList: true,
  subtree: true,
});
