# Craft models

Copies of the AI models that ImageCraft (and the other Craft apps) download, kept here so the apps keep working if an original disappears from Hugging Face or Google. The apps always try the original first; only if that fails do they use these copies.

Each file is stored under its original address (without `https://`), split into parts of at most 45 MB, because GitHub only serves files under 100 MB to web pages. `manifest.json` lists every original address with its size, SHA-256 fingerprint, number of parts and licence. The apps rejoin the parts and check the fingerprint before using a copy, so a broken or altered copy is never loaded.

`mirror.py` makes or refreshes the copies (it only downloads what is missing).

## The models and their licences

| Model | Files | Size | Licence |
| --- | --- | --- | --- |
| CLIPSeg (find things by name) | 8 | 143 MB | Apache-2.0 |
| SlimSAM (pick an object) | 6 | 35 MB | Apache-2.0 |
| Swin2SR 2× (clean pictures) | 4 | 76 MB | Apache-2.0 |
| Swin2SR 4× (old photos) | 4 | 74 MB | Apache-2.0 |
| Swin2SR 4× (JPEG clean-up) | 4 | 77 MB | Apache-2.0 |
| BEN2 (best-quality cut-out) | 3 | 219 MB | MIT |
| U²-Net (background cut-out) | 1 | 176 MB | Apache-2.0 |
| U²-Netp (cut-out, small) | 1 | 5 MB | Apache-2.0 |
| Real-ESRGAN 4× and 2× | 2 | 134 MB | BSD-3-Clause |
| MI-GAN (repair) | 1 | 28 MB | MIT |
| CodeFormer (restore faces) | 1 | 377 MB | S-Lab License 1.0 (non-commercial use only) |
| DDColor-tiny (colourise) | 1 | 135 MB | Apache-2.0 |
| MediaPipe Face Landmarker (face finder) | 1 | 4 MB | Apache-2.0 |

The licence texts are in `licences/`. Every model is shared here under its own licence, unchanged. **CodeFormer is for non-commercial use only** (S-Lab License 1.0). These copies are kept for the non-commercial Craft apps; check each licence before using a model for anything else.

Sources: Xenova and onnx-community ONNX conversions on Hugging Face (Transformers.js), BritishWerewolf (U²-Net), SceneWorks (Real-ESRGAN), andraniksargsyan (MI-GAN pipeline), bluefoxcreation (CodeFormer), edgetools (DDColor-tiny), Google MediaPipe (Face Landmarker). Original projects: CLIPSeg, SlimSAM/Segment Anything, Swin2SR, BEN2, U²-Net, Real-ESRGAN, MI-GAN, CodeFormer, DDColor, MediaPipe.
