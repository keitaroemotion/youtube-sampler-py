# sampler

Youtube -> wav sampler. (wrapping ffmpeg and afplay)
Can download target youtube video to fractions

## installation

``
$ scripts/install
``

## usage

```
$ sampler --play [mp3|wav]                      ... play music file
$ sampler --wav [url1] [url2] ...               ... download YouTube link to wav file
$ sampler --sample [start] [duration] [wavfile] ... sample wav file
```

To sample the music, for example,

```
$ sampler --sample 20 2 
```

## known issues

if the target video's duration is too long, the HTTP 403(Forbidden) Error is givenj.
