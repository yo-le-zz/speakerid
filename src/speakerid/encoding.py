from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from speechbrain.inference.speaker import EncoderClassifier


_MODEL: EncoderClassifier | None = None


def _get_model() -> EncoderClassifier:
    global _MODEL

    if _MODEL is None:
        _MODEL = EncoderClassifier.from_hparams(
            source="speechbrain/spkrec-ecapa-voxceleb",
            savedir="models/spkrec-ecapa-voxceleb",
        )

    return _MODEL


def encode(
    audio: str | Path,
    sample_rate: int = 16000,
) -> np.ndarray:
    """Generate a speaker embedding from an audio file."""

    audio = Path(audio)

    if not audio.exists():
        raise FileNotFoundError(f"Audio file not found: {audio}")

    if not audio.is_file():
        raise ValueError(f"Audio path is not a file: {audio}")

    waveform, input_sample_rate = sf.read(
        audio,
        dtype="float32",
    )

    if waveform.size == 0:
        raise ValueError("Audio file is empty")

    # Convert stereo/multichannel audio to mono.
    if waveform.ndim > 1:
        waveform = waveform.mean(axis=1)

    # Convert NumPy array to PyTorch tensor.
    waveform = torch.from_numpy(waveform)

    # Resample if necessary.
    if input_sample_rate != sample_rate:
        waveform = torch.from_numpy(
            np.array(
                waveform,
                dtype=np.float32,
            )
        )

        waveform = torch.nn.functional.interpolate(
            waveform.unsqueeze(0).unsqueeze(0),
            size=int(
                len(waveform)
                * sample_rate
                / input_sample_rate
            ),
            mode="linear",
            align_corners=False,
        ).squeeze()

    model = _get_model()

    with torch.no_grad():
        embedding = model.encode_batch(
            waveform.unsqueeze(0),
        )

    embedding = embedding.squeeze().cpu().numpy()

    embedding = embedding.astype(np.float32)
    
    norm = np.linalg.norm(embedding)
    
    if norm > 0:
        embedding /= norm
    
    return embedding
    
    return embedding.astype(np.float32)