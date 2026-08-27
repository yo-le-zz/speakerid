# SpeakerID

SpeakerID is a Python library for speaker recognition.

It allows you to create voice profiles, process audio recordings, generate audio variations and identify or verify speakers.

## Features

- 🎙️ Record voice samples
- 📝 Configurable recording phrases
- 🧹 Voice isolation and audio cleaning
- 🔊 Audio augmentation
- 🧠 Speaker embeddings
- 👤 Speaker identification
- ✅ Speaker verification
- 💾 Voice profile management
- 📦 Local storage of speaker profiles
- 🐍 Python API

## Installation

### Using uv

```bash
uv add speakerid
```

### Using pip

```bash
pip install speakerid
```

## Quick start

```python
from speakerid import enroll, identify

enroll("yolezz")

result = identify("test.wav")

if result.known:
    print(f"Speaker: {result.name}")
    print(f"Score: {result.score:.2f}")
else:
    print("Unknown speaker")
```

## Documentation

- [Getting Started](docs/getting-started.md)
- [API Reference](docs/api.md)
- [Examples](docs/examples.md)

## License

See [LICENSE](LICENSE).