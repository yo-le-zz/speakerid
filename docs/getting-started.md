# Getting Started

This guide explains how to install SpeakerID and perform the first speaker recognition test.

## Installation

### Using uv

```bash
uv add speakerid
```

### Using pip

```bash
pip install speakerid
```

## Create a speaker profile

A speaker profile contains the voice samples and embeddings associated with a person.

```python
from speakerid import enroll

enroll("yolezz")
```

SpeakerID will guide the user through the recording process.

The default process records several samples using different phrases.

The generated profile can look like:

```text
voices/
└── yolezz/
    ├── samples/
    │   ├── sample_01.wav
    │   ├── sample_02.wav
    │   └── sample_03.wav
    ├── augmented/
    │   ├── sample_01_01.wav
    │   └── ...
    └── profile.json
```

## Use custom phrases

You can provide your own phrases when enrolling a speaker.

```python
from speakerid import enroll

enroll(
    "yolezz",
    phrases=[
        "Bonjour, je m'appelle Yolezz.",
        "Le soleil brille aujourd'hui.",
        "Cette phrase permet d'identifier ma voix.",
    ],
)
```

You can also configure the default phrases:

```python
from speakerid import set_phrases

set_phrases(
    [
        "Bonjour, je m'appelle Yolezz.",
        "Le ciel est particulièrement bleu aujourd'hui.",
        "Cette phrase permet de tester ma voix.",
    ],
    language="fr",
)
```

## Record a voice manually

```python
from speakerid import record

path = record(
    output="voice.wav",
    duration=5,
)

print(path)
```

You can also display a phrase before recording:

```python
record(
    output="voice.wav",
    duration=5,
    phrase="Bonjour, je m'appelle Yolezz.",
)
```

## Clean an audio file

```python
from speakerid import clean

clean(
    input="raw.wav",
    output="clean.wav",
)
```

By default, SpeakerID can:

- Reduce background noise
- Normalize the volume
- Remove unnecessary silence
- Apply a high-pass filter

## Generate audio variations

Audio augmentation can be used to create variations of a voice sample.

```python
from speakerid import augment

augment(
    input="voice.wav",
    output_dir="augmented/",
    count=10,
)
```

The generated files can contain controlled variations such as:

- Background noise
- Reverb
- Speed changes
- Pitch changes
- Volume changes

## Generate an embedding

An embedding is a numerical representation of a speaker's voice.

```python
from speakerid import encode

embedding = encode("voice.wav")

print(embedding)
```

Embeddings are used internally for speaker comparison and identification.

## Compare two voices

```python
from speakerid import compare

score = compare(
    "voice_1.wav",
    "voice_2.wav",
)

print(score)
```

A higher score means that the two voices are more similar according to the configured speaker model.

## Identify a speaker

```python
from speakerid import identify

result = identify("test.wav")

print(result.name)
print(result.score)
print(result.known)
```

If no profile reaches the configured threshold:

```text
name = None
known = False
```

## Verify a speaker

Verification answers:

> Is this voice from this specific person?

```python
from speakerid import verify

result = verify(
    "test.wav",
    "yolezz",
)

print(result.match)
print(result.score)
```

## Next steps

See the [API Reference](api.md) for all available functions.

See [Examples](examples.md) for complete usage examples.