import json,wave,subprocess,os,re,sys,base64,hashlib
from piper import PiperVoice,SynthesisConfig
V=PiperVoice.load("/home/claude/tts/en-us-lessac-medium.onnx")
words=json.load(open("/home/claude/words.json"))
html=open("/home/claude/spelling-fishing.html").read()
# pull SAY map from game source
say=dict(re.findall(r'"([^"]+)":"([^"]+)"',html[html.index("const SAY"):html.index("/* ---------- state")]))
letters={c:c.upper() for c in "abcdefghijklmnopqrstuvwxyz"}
clips={}
for w in words:
    clips["b:"+w]=(w+".",1.12)
    clips["s:"+w]=(w+".",1.7)
    if w in say and say[w]!=w: clips["h:"+w]=(say[w]+".",1.08)
for k,t in letters.items(): clips["l:"+k]=(t+".",1.15)
for k,t in {"go":"Let's go fishing!","oops":"Oops, that's","try":"Try again!","next":"The next letter is","perfect":"Perfect!","great":"Great job!","fishing":"Great fishing!","nice":"Nice catch!"}.items(): clips["p:"+k]=(t,1.0)
out={}
for i,(k,(t,ls)) in enumerate(clips.items()):
    fn="/home/claude/clips/"+hashlib.md5(k.encode()).hexdigest()
    with wave.open(fn+".wav","wb") as wf: V.synthesize_wav(t,wf,syn_config=SynthesisConfig(length_scale=ls,noise_scale=0.5,noise_w_scale=0.6))
    subprocess.run(["ffmpeg","-loglevel","error","-y","-i",fn+".wav","-af","silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=0.05","-ac","1","-ar","22050","-b:a","48k",fn+".mp3"],check=True)
    out[k]=base64.b64encode(open(fn+".mp3","rb").read()).decode()
json.dump(out,open("/home/claude/clips.json","w"))
print(len(out), sum(len(v) for v in out.values())/1e6,"MB b64")
