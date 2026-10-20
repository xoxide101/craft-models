# Copies the AI models ImageCraft (and the other Craft apps) download, so they keep working if a source disappears.
# Each file is stored under its original address (without "https://"), split into parts of at most 45 MB (GitHub
# serves files under 100 MB to browsers from raw.githubusercontent.com), with its size and SHA-256 in manifest.json.
# Usage: python mirror.py            (downloads what is missing, then writes manifest.json)
import hashlib, json, os, sys, urllib.request
PART = 45 * 1024 * 1024
HF = 'https://huggingface.co/{}/resolve/main/{}'
FILES = {
  'Xenova/clipseg-rd64-refined': (['config.json', 'preprocessor_config.json', 'tokenizer.json', 'tokenizer_config.json', 'special_tokens_map.json', 'merges.txt', 'vocab.json', 'onnx/model_quantized.onnx'], 'Apache-2.0', 'CLIPSeg (find things by name)'),
  'Xenova/slimsam-77-uniform': (['config.json', 'preprocessor_config.json', 'onnx/vision_encoder_fp16.onnx', 'onnx/prompt_encoder_mask_decoder_fp16.onnx', 'onnx/vision_encoder_quantized.onnx', 'onnx/prompt_encoder_mask_decoder_quantized.onnx'], 'Apache-2.0', 'SlimSAM (pick an object)'),
  'Xenova/swin2SR-classical-sr-x2-64': (['config.json', 'preprocessor_config.json', 'onnx/model.onnx', 'onnx/model_quantized.onnx'], 'Apache-2.0', 'Swin2SR 2× (clean pictures)'),
  'Xenova/swin2SR-realworld-sr-x4-64-bsrgan-psnr': (['config.json', 'preprocessor_config.json', 'onnx/model.onnx', 'onnx/model_quantized.onnx'], 'Apache-2.0', 'Swin2SR 4× (old photos)'),
  'Xenova/swin2SR-compressed-sr-x4-48': (['config.json', 'preprocessor_config.json', 'onnx/model.onnx', 'onnx/model_quantized.onnx'], 'Apache-2.0', 'Swin2SR 4× (JPEG clean-up)'),
  'onnx-community/BEN2-ONNX': (['config.json', 'preprocessor_config.json', 'onnx/model_fp16.onnx'], 'MIT', 'BEN2 (best-quality cut-out)'),
  'BritishWerewolf/U-2-Net': (['onnx/model.onnx'], 'Apache-2.0', 'U²-Net (background cut-out)'),
  'BritishWerewolf/U-2-Netp': (['onnx/model.onnx'], 'Apache-2.0', 'U²-Netp (cut-out, small)'),
  'SceneWorks/real-esrgan-onnx': (['real_esrgan_x4.onnx', 'real_esrgan_x2.onnx'], 'BSD-3-Clause', 'Real-ESRGAN 4× and 2×'),
  'andraniksargsyan/migan': (['migan_pipeline_v2.onnx'], 'MIT', 'MI-GAN (repair)'),
  'bluefoxcreation/Codeformer-ONNX': (['codeformer.onnx'], 'S-Lab License 1.0 (non-commercial use only)', 'CodeFormer (restore faces)'),
  'edgetools/ddcolor': (['ddcolor-tiny-fp16.onnx'], 'Apache-2.0', 'DDColor-tiny (colourise)'),
}
OTHER = [('https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task', 'Apache-2.0', 'MediaPipe Face Landmarker (face finder)')]
urls = [(HF.format(repo, f), lic, what) for repo, (fs, lic, what) in FILES.items() for f in fs] + OTHER
man = json.load(open('manifest.json')) if os.path.exists('manifest.json') else {}
for url, lic, what in urls:
    path = url.split('://', 1)[1]
    if url in man and all(os.path.exists(f'{path}.part{i:03d}') for i in range(man[url]['parts'])): continue
    print('fetching', url, flush=True)
    data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'craft-models-mirror'}), timeout=600).read()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    n = max(1, -(-len(data) // PART))
    for i in range(n): open(f'{path}.part{i:03d}', 'wb').write(data[i * PART:(i + 1) * PART])
    man[url] = {'size': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'parts': n, 'licence': lic, 'what': what}
    json.dump(man, open('manifest.json', 'w'), indent=1)
print(len(man), 'files,', round(sum(v['size'] for v in man.values()) / 1e9, 2), 'GB')
