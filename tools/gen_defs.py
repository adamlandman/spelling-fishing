import json,wave,subprocess,base64,hashlib
from piper import PiperVoice,SynthesisConfig
V=PiperVoice.load("/home/claude/tts/en-us-lessac-medium.onnx")
d=json.load(open("/home/claude/defs.json")); out=json.load(open("/home/claude/clips.json"))
items={"d:"+w:(v[1].replace(";",",")+".",1.08) for w,v in d.items()}
items["p:means"]=("It means:",1.05)
for k,(t,ls) in items.items():
    fn="/home/claude/clips/"+hashlib.md5(k.encode()).hexdigest()
    with wave.open(fn+".wav","wb") as wf: V.synthesize_wav(t,wf,syn_config=SynthesisConfig(length_scale=ls,noise_scale=0.5,noise_w_scale=0.6))
    subprocess.run(["ffmpeg","-loglevel","error","-y","-i",fn+".wav","-af","silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=0.05","-ac","1","-ar","22050","-b:a","32k",fn+".mp3"],check=True)
    out[k]=base64.b64encode(open(fn+".mp3","rb").read()).decode()
json.dump(out,open("/home/claude/clips.json","w")); print(len(out),sum(map(len,out.values()))/1e6)
