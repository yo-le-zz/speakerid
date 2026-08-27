# API Reference

This document contains the complete public API of SpeakerID.

## record

Records audio from a microphone.

### Arguments

- `output` → output WAV file
- `duration` → recording duration in seconds
- `sample_rate` → audio sample rate
- `channels` → number of audio channels
- `device` → microphone to use
- `phrase` → optional phrase displayed before recording

### Example

```python
from speakerid import record

record(
    output="voice.wav",
    duration=5.0,
    sample_rate=16000,
    channels=1,
    device=None,
    phrase=None,
)
```

### Returns

```python
Path
```

---

## set_phrases

Sets the phrases used during speaker enrollment.

### Arguments

- `phrases` → list of phrases
- `language` → language of the phrases

### Example

```python
from speakerid import set_phrases

set_phrases(
    phrases=[
        "Bonjour, je m'appelle Yolezz.",
        "Le soleil brille aujourd'hui.",
    ],
    language="fr",
)
```

---

## get_phrases

Returns the configured phrases.

### Arguments

- `language` → language to retrieve

### Example

```python
from speakerid import get_phrases

phrases = get_phrases(
    language="fr",
)

print(phrases)
```

### Returns

```python
list[str]
```

---

## enroll

Creates a complete voice profile for a speaker.

### Arguments

- `name` → speaker name
- `samples` → number of recordings
- `output_dir` → profile storage directory
- `clean` → enable audio cleaning
- `augment` → enable audio augmentation
- `augmentation_count` → number of variants generated per sample
- `phrases` → custom phrases

### Example

```python
from speakerid import enroll

profile = enroll(
    name="yolezz",
    samples=5,
    output_dir="voices",
    clean=True,
    augment=True,
    augmentation_count=3,
    phrases=None,
)
```

### Returns

```python
VoiceProfile
```

---

## clean

Cleans and processes an audio file.

### Arguments

- `input` → input audio file
- `output` → output audio file
- `noise_reduction` → enable noise reduction
- `normalize` → normalize audio volume
- `remove_silence` → remove unnecessary silence
- `highpass` → enable high-pass filtering

### Example

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

### Returns

```python
Path
```

---

## augment

Generates variations of an audio file.

### Arguments

- `input` → input audio file
- `output_dir` → directory for generated files
- `count` → number of variants
- `noise` → enable noise augmentation
- `reverb` → enable reverb augmentation
- `speed` → enable speed augmentation
- `pitch` → enable pitch augmentation
- `volume` → enable volume augmentation

### Example

```python
from speakerid import augment

files = augment(
    input="voice.wav",
    output_dir="augmented",
    count=10,
    noise=True,
    reverb=True,
    speed=True,
    pitch=True,
    volume=True,
)
```

### Returns

```python
list[Path]
```

---

## encode

Generates a speaker embedding from an audio file.

### Arguments

- `audio` → audio file
- `sample_rate` → audio sample rate

### Example

```python
from speakerid import encode

embedding = encode(
    audio="voice.wav",
    sample_rate=16000,
)
```

### Returns

```python
Embedding
```

---

## compare

Compares two voices.

### Arguments

- `audio_a` → first audio file or embedding
- `audio_b` → second audio file or embedding

### Example

```python
from speakerid import compare

score = compare(
    audio_a="voice_1.wav",
    audio_b="voice_2.wav",
)

print(score)
```

### Returns

```python
float
```

---

## identify

Identifies a speaker from the available profiles.

### Arguments

- `audio` → audio file to identify
- `threshold` → minimum similarity score
- `profiles` → profiles to check, or all profiles when `None`

### Example

```python
from speakerid import identify

result = identify(
    audio="test.wav",
    threshold=0.70,
)

print(result.name)
print(result.score)
print(result.known)
```

### Returns

```python
SpeakerResult
```

---

## verify

Verifies whether an audio sample belongs to a specific speaker.

### Arguments

- `audio` → audio file to verify
- `speaker` → speaker name
- `threshold` → minimum similarity score

### Example

```python
from speakerid import verify

result = verify(
    audio="test.wav",
    speaker="yolezz",
    threshold=0.70,
)

print(result.match)
print(result.score)
```

### Returns

```python
VerificationResult
```

---

## get_profile

Returns a speaker profile.

### Arguments

- `name` → speaker name

### Example

```python
from speakerid import get_profile

profile = get_profile("yolezz")
```

### Returns

```python
VoiceProfile | None
```

---

## list_profiles

Returns all registered speaker profiles.

### Arguments

None.

### Example

```python
from speakerid import list_profiles

profiles = list_profiles()

for profile in profiles:
    print(profile.name)
```

### Returns

```python
list[VoiceProfile]
```

---

## add_sample

Adds an audio sample to an existing speaker profile.

### Arguments

- `speaker` → speaker name
- `audio` → audio file
- `clean` → enable audio cleaning
- `augment` → generate augmented samples
- `augmentation_count` → number of generated variants

### Example

```python
from speakerid import add_sample

add_sample(
    speaker="yolezz",
    audio="new_voice.wav",
    clean=True,
    augment=False,
    augmentation_count=3,
)
```

---

## remove_sample

Removes a sample from a speaker profile.

### Arguments

- `speaker` → speaker name
- `sample` → sample file or sample identifier

### Example

```python
from speakerid import remove_sample

remove_sample(
    speaker="yolezz",
    sample="sample_01.wav",
)
```

---

## build_profile

Rebuilds a speaker profile from its available samples.

### Arguments

- `speaker` → speaker name
- `use_augmented` → include augmented samples

### Example

```python
from speakerid import build_profile

profile = build_profile(
    speaker="yolezz",
    use_augmented=True,
)
```

### Returns

```python
VoiceProfile
```

---

## delete_profile

Deletes a speaker profile.

### Arguments

- `name` → speaker name
- `delete_audio` → also delete associated audio files

### Example

```python
from speakerid import delete_profile

delete_profile(
    name="yolezz",
    delete_audio=True,
)
```

---

## save

Saves the speaker database.

### Arguments

- `path` → database directory

### Example

```python
from speakerid import save

save(
    path="speakerdb",
)
```

---

## load

Loads a speaker database.

### Arguments

- `path` → database directory

### Example

```python
from speakerid import load

load(
    path="speakerdb",
)
```