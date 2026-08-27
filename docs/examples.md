# Examples

This document contains complete examples using SpeakerID.

## Basic speaker identification

```python
from speakerid import enroll, identify

enroll("yolezz")

result = identify("test.wav")

if result.known:
    print(f"Speaker: {result.name}")
    print(f"Confidence: {result.score:.2%}")
else:
    print("Unknown speaker")
```

## Multiple speakers

```python
from speakerid import enroll, identify

enroll("yolezz")
enroll("alice")
enroll("bob")

result = identify("test.wav")

if result.known:
    print(f"Detected speaker: {result.name}")
    print(f"Score: {result.score:.2%}")
else:
    print("Unknown speaker")
```

## Recording a voice

```python
from speakerid import record

path = record(
    output="voice.wav",
    duration=5,
)

print(f"Saved to: {path}")
```

## Recording with a phrase

```python
from speakerid import record

record(
    output="voice.wav",
    duration=5,
)
```

## Custom enrollment phrases

```python
from speakerid import enroll

profile = enroll(
    name="yolezz",
    samples=10,
    phrases=[
        "Bonjour, je m'appelle Yolezz.",
        "Le soleil brille aujourd'hui.",
        "J'aime programmer en Python.",
        "Cette phrase permet de tester ma voix.",
        "Les ordinateurs sont fascinants.",
    ],
)
```

## Cleaning an audio file

```python
from speakerid import clean

clean(
    input="raw.wav",
    output="clean.wav",
    noise_reduction=True,
    normalize=True,
    remove_silence=True,
    highpass=True,
)
```

## Audio augmentation

```python
from speakerid import augment

files = augment(
    input="voice.wav",
    output_dir="augmented",
    count=20,
)

for file in files:
    print(file)
```

## Compare two recordings

```python
from speakerid import compare

score = compare(
    "voice_1.wav",
    "voice_2.wav",
)

print(f"Similarity: {score:.2%}")
```

## Verify a speaker

```python
from speakerid import verify

result = verify(
    audio="test.wav",
    speaker="yolezz",
)

if result.match:
    print("The speaker is probably Yolezz.")
else:
    print("The speaker does not match Yolezz.")
```

## Working with profiles

```python
from speakerid import (
    add_sample,
    delete_profile,
    get_profile,
    list_profiles,
)

profile = get_profile("yolezz")

if profile:
    print(profile.name)

add_sample(
    speaker="yolezz",
    audio="new_voice.wav",
)

for profile in list_profiles():
    print(profile.name)

delete_profile(
    name="yolezz",
)
```

## Save and load a database

```python
from speakerid import save, load

save("speakerdb")

load("speakerdb")
```

## Complete workflow

```python
from speakerid import (
    enroll,
    identify,
)

# Create the speaker profile.
enroll(
    name="yolezz",
    samples=10,
    clean=True,
    augment=True,
    augmentation_count=5,
)

# Identify a new recording.
result = identify(
    "test.wav",
    threshold=0.70,
)

if result.known:
    print(
        f"Detected: {result.name} "
        f"({result.score:.2%})"
    )
else:
    print("Unknown speaker")
```