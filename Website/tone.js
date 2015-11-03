
// Example showing how to produce a tone using Web Audio API.
// Load the file webaudio_tools.js before loading this file.
// This code will write to a DIV with an id="soundStatus".
var oscillator;
var amp;

// Create an oscillator and an amplifier.
function initAudio()
{
	// Use audioContext from webaudio_tools.js
	if( audioContext )
	{
		oscillator = audioContext.createOscillator();
		fixOscillator(oscillator);
		oscillator.frequency.value = 440;
		amp = audioContext.createGain();
		amp.gain.value = 0;
	
		// Connect oscillator to amp and amp to the mixer of the audioContext.
		// This is like connecting cables between jacks on a modular synth.
		oscillator.connect(amp);
		amp.connect(audioContext.destination);
		oscillator.start(0);
		writeMessageToID( "soundStatus", "<p>Audio initialized.</p>");
	}
}

// Set the frequency of the oscillator and start it running.
function startTone( frequency )
{
	var now = audioContext.currentTime;
	
	oscillator.frequency.setValueAtTime(frequency, now);
	
	// Ramp up the gain so we can hear the sound.
	// We can ramp smoothly to the desired value.
	// First we should cancel any previous scheduled events that might interfere.
	amp.gain.cancelScheduledValues(now);
	// Anchor beginning of ramp at current value.
	amp.gain.setValueAtTime(amp.gain.value, now);
	amp.gain.linearRampToValueAtTime(0.5, audioContext.currentTime + 0.001);
	
	writeMessageToID( "soundStatus", "<p>Play tone at frequency = " + frequency  + "</p>");
}

function sleep(ms)
{
	var dt = new Date();
	dt.setTime(dt.getTime() + ms);
	while (new Date().getTime() < dt.getTime());
}

function playTone( frequency, time )
{
	var now = audioContext.currentTime;
	
	oscillator.frequency.setValueAtTime(frequency, now);
	
	// Ramp up the gain so we can hear the sound.
	// We can ramp smoothly to the desired value.
	// First we should cancel any previous scheduled events that might interfere.
	amp.gain.cancelScheduledValues(now);
	// Anchor beginning of ramp at current value.
	amp.gain.setValueAtTime(amp.gain.value, now);
	amp.gain.linearRampToValueAtTime(0.5, audioContext.currentTime + 0.001);
	sleep(time);
	now = audioContext.currentTime;
	amp.gain.cancelScheduledValues(now);
	amp.gain.setValueAtTime(amp.gain.value, now);
	amp.gain.linearRampToValueAtTime(0.0, audioContext.currentTime + 0.1);
	writeMessageToID( "soundStatus", "<p>Stop tone.</p>");
	
	writeMessageToID( "soundStatus", "<p>Play tone at frequency = " + frequency  + "</p>");	
}
function playText( stringText )
{
	for (var i = stringText.length - 1; i >= 0; i--) {
		if (stringText[stringText.length - 1 - i] == " "){
			playTone(0,250)
		}
		else{
			playTone(((stringText[stringText.length - 1 - i].charCodeAt(0))-32)*32, 250)
		}
	};
}


function repeatTone( frequency, time )
{
	var startTime = context.currentTime + 0.100;
    var tempo = 80; // BPM (beats per minute)
    var eighthNoteTime = (60 / tempo) / 2;

	for (var bar = 0; bar < 2; bar++) {
  		var time = startTime + bar * 8 * 8;
		playTone(frequency,time);
		sleep(time)
	}
}

function stopTone()
{
	var now = audioContext.currentTime;
	amp.gain.cancelScheduledValues(now);
	amp.gain.setValueAtTime(amp.gain.value, now);
	amp.gain.linearRampToValueAtTime(0.0, audioContext.currentTime + 0.05);
	writeMessageToID( "soundStatus", "<p>Stop tone.</p>");
}

function repeatbeat()
{

}

// init once the page has finished loading.
window.onload = initAudio;
