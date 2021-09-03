'''Audio System (aud)
   Audaspace (pronounced "outer space") is a high level audio library.
   
'''


AP_LOCATION = 3 #constant value 

AP_ORIENTATION = 4 #constant value 

AP_PANNING = 1 #constant value 

AP_PITCH = 2 #constant value 

AP_VOLUME = 0 #constant value 

CHANNELS_INVALID = 0 #constant value 

CHANNELS_MONO = 1 #constant value 

CHANNELS_STEREO = 2 #constant value 

CHANNELS_STEREO_LFE = 3 #constant value 

CHANNELS_SURROUND4 = 4 #constant value 

CHANNELS_SURROUND5 = 5 #constant value 

CHANNELS_SURROUND51 = 6 #constant value 

CHANNELS_SURROUND61 = 7 #constant value 

CHANNELS_SURROUND71 = 8 #constant value 

CODEC_AAC = 1 #constant value 

CODEC_AC3 = 2 #constant value 

CODEC_FLAC = 3 #constant value 

CODEC_INVALID = 0 #constant value 

CODEC_MP2 = 4 #constant value 

CODEC_MP3 = 5 #constant value 

CODEC_OPUS = 8 #constant value 

CODEC_PCM = 6 #constant value 

CODEC_VORBIS = 7 #constant value 

CONTAINER_AC3 = 1 #constant value 

CONTAINER_FLAC = 2 #constant value 

CONTAINER_INVALID = 0 #constant value 

CONTAINER_MATROSKA = 3 #constant value 

CONTAINER_MP2 = 4 #constant value 

CONTAINER_MP3 = 5 #constant value 

CONTAINER_OGG = 6 #constant value 

CONTAINER_WAV = 7 #constant value 

DISTANCE_MODEL_EXPONENT = 5 #constant value 

DISTANCE_MODEL_EXPONENT_CLAMPED = 6 #constant value 

DISTANCE_MODEL_INVALID = 0 #constant value 

DISTANCE_MODEL_INVERSE = 1 #constant value 

DISTANCE_MODEL_INVERSE_CLAMPED = 2 #constant value 

DISTANCE_MODEL_LINEAR = 3 #constant value 

DISTANCE_MODEL_LINEAR_CLAMPED = 4 #constant value 

FORMAT_FLOAT32 = 36 #constant value 

FORMAT_FLOAT64 = 40 #constant value 

FORMAT_INVALID = 0 #constant value 

FORMAT_S16 = 18 #constant value 

FORMAT_S24 = 19 #constant value 

FORMAT_S32 = 20 #constant value 

FORMAT_U8 = 1 #constant value 

RATE_11025 = 11025 #constant value 

RATE_16000 = 16000 #constant value 

RATE_192000 = 192000 #constant value 

RATE_22050 = 22050 #constant value 

RATE_32000 = 32000 #constant value 

RATE_44100 = 44100 #constant value 

RATE_48000 = 48000 #constant value 

RATE_8000 = 8000 #constant value 

RATE_88200 = 88200 #constant value 

RATE_96000 = 96000 #constant value 

RATE_INVALID = 0 #constant value 

STATUS_INVALID = 0 #constant value 

STATUS_PAUSED = 2 #constant value 

STATUS_PLAYING = 1 #constant value 

STATUS_STOPPED = 3 #constant value 

class Device:
   '''Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.
      
   '''

   def lock():
      '''Locks the device so that it's guaranteed, that no samples are
         read from the streams until :meth:unlock is called.
         This is useful if you want to do start/stop/pause/resume some
         sounds at the same time.
         .. note::
         The device has to be unlocked as often as locked to be
         able to continue playback.
         .. warning::
         Make sure the time between locking and unlocking is
         as short as possible to avoid clicks.
         
      '''
   
      pass
   

   def play(sound, keep=False):
      '''Plays a sound.
         
         Arguments:
         @sound (Sound): The sound to play.
         @keep (bool): See :attr:Handle.keep.
   
         @returns (Handle): The playback handle with which playback can becontrolled with.
         
      '''
   
      return Handle
   

   def stopAll():
      '''Stops all playing and paused sounds.
         
      '''
   
      pass
   

   def unlock():
      '''Unlocks the device after a lock call, see :meth:lock for
         details.
         
      '''
   
      pass
   

   channels = None
   '''The channel count of the device.
      
   '''
   

   distance_model = None
   '''The distance model of the device.
      
      (seealso OpenAL Documentation <https://www.openal.org/documentation/>__)
      
   '''
   

   doppler_factor = None
   '''The doppler factor of the device.
      This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity.
      
   '''
   

   format = None
   '''The native sample format of the device.
      
   '''
   

   listener_location = None
   '''The listeners's location in 3D space, a 3D tuple of floats.
      
   '''
   

   listener_orientation = None
   '''The listener's orientation in 3D space as quaternion, a 4 float tuple.
      
   '''
   

   listener_velocity = None
   '''The listener's velocity in 3D space, a 3D tuple of floats.
      
   '''
   

   rate = None
   '''The sampling rate of the device in Hz.
      
   '''
   

   speed_of_sound = None
   '''The speed of sound of the device.
      The speed of sound in air is typically 343.3 m/s.
      
   '''
   

   volume = None
   '''The overall volume of the device.
      
   '''
   



class DynamicMusic:
   '''The DynamicMusic object allows to play music depending on a current scene, scene changes are managed by the class, with the possibility of custom transitions.
      The default transition is a crossfade effect, and the default scene is silent and has id 0
      
   '''

   def addScene(scene):
      '''Adds a new scene.
         
         Arguments:
         @scene (Sound): The scene sound.
   
         @returns (int): The new scene id.
      '''
   
      return int
   

   def addTransition(ini, end, transition):
      '''Adds a new scene.
         
         Arguments:
         @ini (int): the initial scene foor the transition.
         @end (int): The final scene for the transition.
         @transition (Sound): The transition sound.
   
         @returns (bool): false if the ini or end scenes don't exist, true othrwise.
      '''
   
      return bool
   

   def pause():
      '''Pauses playback of the scene.
         
         @returns (bool): Whether the action succeeded.
      '''
   
      return bool
   

   def resume():
      '''Resumes playback of the scene.
         
         @returns (bool): Whether the action succeeded.
      '''
   
      return bool
   

   def stop():
      '''Stops playback of the scene.
         
         @returns (bool): Whether the action succeeded.
      '''
   
      return bool
   

   fadeTime = None
   '''The length in seconds of the crossfade transition
      
   '''
   

   position = None
   '''The playback position of the scene in seconds.
      
   '''
   

   scene = None
   '''The current scene
      
   '''
   

   status = None
   '''Whether the scene is playing, paused or stopped (=invalid).
      
   '''
   

   volume = None
   '''The volume of the scene.
      
   '''
   



class Handle:
   '''Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.
      
   '''

   def pause():
      '''Pauses playback.
         
         @returns (bool): Whether the action succeeded.
      '''
   
      return bool
   

   def resume():
      '''Resumes playback.
         
         @returns (bool): Whether the action succeeded.
      '''
   
      return bool
   

   def stop():
      '''Stops playback.
         
         @returns (bool): Whether the action succeeded.
         Note: This makes the handle invalid.
      '''
   
      return bool
   

   attenuation = None
   '''This factor is used for distance based attenuation of the source.
      
      (seealso :attr:Device.distance_model)
      
   '''
   

   cone_angle_inner = None
   '''The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the :attr:location of the source and with infinite height, heading in the direction of the source's :attr:orientation.
      In the inner cone the volume is normal. Outside the outer cone the volume will be :attr:cone_volume_outer and in the area between the volume will be interpolated linearly.
      
   '''
   

   cone_angle_outer = None
   '''The opening angle of the outer cone of the source.
      
      (seealso :attr:cone_angle_inner)
      
   '''
   

   cone_volume_outer = None
   '''The volume outside the outer cone of the source.
      
      (seealso :attr:cone_angle_inner)
      
   '''
   

   distance_maximum = None
   '''The maximum distance of the source.
      If the listener is further away the source volume will be 0.
      
      (seealso :attr:Device.distance_model)
      
   '''
   

   distance_reference = None
   '''The reference distance of the source.
      At this distance the volume will be exactly :attr:volume.
      
      (seealso :attr:Device.distance_model)
      
   '''
   

   keep = None
   '''Whether the sound should be kept paused in the device when its end is reached.
      This can be used to seek the sound to some position and start playback again.
      .. warning:: If this is set to true and you forget stopping this equals a memory leak as the handle exists until the device is destroyed.
      
   '''
   

   location = None
   '''The source's location in 3D space, a 3D tuple of floats.
      
   '''
   

   loop_count = None
   '''The (remaining) loop count of the sound. A negative value indicates infinity.
      
   '''
   

   orientation = None
   '''The source's orientation in 3D space as quaternion, a 4 float tuple.
      
   '''
   

   pitch = None
   '''The pitch of the sound.
      
   '''
   

   position = None
   '''The playback position of the sound in seconds.
      
   '''
   

   relative = None
   '''Whether the source's location, velocity and orientation is relative or absolute to the listener.
      
   '''
   

   status = None
   '''Whether the sound is playing, paused or stopped (=invalid).
      
   '''
   

   velocity = None
   '''The source's velocity in 3D space, a 3D tuple of floats.
      
   '''
   

   volume = None
   '''The volume of the sound.
      
   '''
   

   volume_maximum = None
   '''The maximum volume of the source.
      
      (seealso :attr:Device.distance_model)
      
   '''
   

   volume_minimum = None
   '''The minimum volume of the source.
      
      (seealso :attr:Device.distance_model)
      
   '''
   



class PlaybackManager:
   '''A PlabackManager object allows to easily control groups os sounds organized in categories.
      
   '''

   def addCategory(volume):
      '''Adds a category with a custom volume.
         
         Arguments:
         @volume (float): The volume for ther new category.
   
         @returns (int): The key of the new category.
      '''
   
      return int
   

   def clean():
      '''Cleans all the invalid and finished sound from the playback manager.
         
      '''
   
      pass
   

   def getVolume(catKey):
      '''Retrieves the volume of a category.
         
         Arguments:
         @catKey (int): the key of the category.
   
         @returns (float): The volume of the cateogry.
      '''
   
      return float
   

   def pause(catKey):
      '''Pauses playback of the category.
         
         Arguments:
         @catKey (int): the key of the category.
   
         @returns (bool): Whether the action succeeded.
      '''
   
      return bool
   

   def setVolume(sound, catKey):
      '''Plays a sound through the playback manager and assigns it to a category.
         
         Arguments:
         @sound (Sound): The sound to play.
         @catKey (int): the key of the category in which the sound will be added,if it doesn't exist, a new one will be created.
         
   
         @returns (Handle): The playback handle with which playback can be controlled with.
      '''
   
      return Handle
   

   def resume(catKey):
      '''Resumes playback of the catgory.
         
         Arguments:
         @catKey (int): the key of the category.
   
         @returns (bool): Whether the action succeeded.
      '''
   
      return bool
   

   def setVolume(volume, catKey):
      '''Changes the volume of a category.
         
         Arguments:
         @volume (float): the new volume value.
         @catKey (int): the key of the category.
   
         @returns (int): Whether the action succeeded.
      '''
   
      return int
   

   def stop(catKey):
      '''Stops playback of the category.
         
         Arguments:
         @catKey (int): the key of the category.
   
         @returns (bool): Whether the action succeeded.
      '''
   
      return bool
   



class Sequence:
   '''This sound represents sequenced entries to play a sound sequence.
      
   '''

   def add():
      '''Adds a new entry to the sequence.
         
         Arguments:
         @sound (Sound): The sound this entry should play.
         @begin (float): The start time.
         @end (float): The end time or a negative value if determined by the sound.
         @skip (float): How much seconds should be skipped at the beginning.
   
         @returns (SequenceEntry): The entry added.
      '''
   
      return SequenceEntry
   

   def remove():
      '''Removes an entry from the sequence.
         
         Arguments:
         @entry (SequenceEntry): The entry to remove.
   
      '''
   
      pass
   

   def setAnimationData():
      '''Writes animation data to a sequence.
         
         Arguments:
         @type (int): The type of animation data.
         @frame (int): The frame this data is for.
         @data (sequence of float): The data to write.
         @animated (bool): Whether the attribute is animated.
   
      '''
   
      pass
   

   channels = None
   '''The channel count of the sequence.
      
   '''
   

   distance_model = None
   '''The distance model of the sequence.
      
      (seealso OpenAL Documentation <https://www.openal.org/documentation/>__)
      
   '''
   

   doppler_factor = None
   '''The doppler factor of the sequence.
      This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity.
      
   '''
   

   fps = None
   '''The listeners's location in 3D space, a 3D tuple of floats.
      
   '''
   

   muted = None
   '''Whether the whole sequence is muted.
      
   '''
   

   rate = None
   '''The sampling rate of the sequence in Hz.
      
   '''
   

   speed_of_sound = None
   '''The speed of sound of the sequence.
      The speed of sound in air is typically 343.3 m/s.
      
   '''
   



class SequenceEntry:
   '''SequenceEntry objects represent an entry of a sequenced sound.
      
   '''

   def move():
      '''Moves the entry.
         
         Arguments:
         @begin (float): The new start time.
         @end (float): The new end time or a negative value if unknown.
         @skip (float): How many seconds to skip at the beginning.
   
      '''
   
      pass
   

   def setAnimationData():
      '''Writes animation data to a sequenced entry.
         
         Arguments:
         @type (int): The type of animation data.
         @frame (int): The frame this data is for.
         @data (sequence of float): The data to write.
         @animated (bool): Whether the attribute is animated.
   
      '''
   
      pass
   

   attenuation = None
   '''This factor is used for distance based attenuation of the source.
      
      (seealso :attr:Device.distance_model)
      
   '''
   

   cone_angle_inner = None
   '''The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the :attr:location of the source and with infinite height, heading in the direction of the source's :attr:orientation.
      In the inner cone the volume is normal. Outside the outer cone the volume will be :attr:cone_volume_outer and in the area between the volume will be interpolated linearly.
      
   '''
   

   cone_angle_outer = None
   '''The opening angle of the outer cone of the source.
      
      (seealso :attr:cone_angle_inner)
      
   '''
   

   cone_volume_outer = None
   '''The volume outside the outer cone of the source.
      
      (seealso :attr:cone_angle_inner)
      
   '''
   

   distance_maximum = None
   '''The maximum distance of the source.
      If the listener is further away the source volume will be 0.
      
      (seealso :attr:Device.distance_model)
      
   '''
   

   distance_reference = None
   '''The reference distance of the source.
      At this distance the volume will be exactly :attr:volume.
      
      (seealso :attr:Device.distance_model)
      
   '''
   

   muted = None
   '''Whether the entry is muted.
      
   '''
   

   relative = None
   '''Whether the source's location, velocity and orientation is relative or absolute to the listener.
      
   '''
   

   sound = None
   '''The sound the entry is representing and will be played in the sequence.
      
   '''
   

   volume_maximum = None
   '''The maximum volume of the source.
      
      (seealso :attr:Device.distance_model)
      
   '''
   

   volume_minimum = None
   '''The minimum volume of the source.
      
      (seealso :attr:Device.distance_model)
      
   '''
   



class Sound:
   '''Sound objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback.
      
   '''

   @classmethod
   def buffer(data, rate):
      '''Creates a sound from a data buffer.
         
         Arguments:
         @data (numpy.ndarray): The data as two dimensional numpy array.
         @rate (double): The sample rate.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   @classmethod
   def file(filename):
      '''Creates a sound object of a sound file.
         
         Arguments:
         @filename (string): Path of the file.
   
         @returns (Sound): The created Sound object... warning::
         If the file doesn't exist or can't be read you will
         not get an exception immediately, but when you try to start
         playback of that sound.
         
      '''
   
      return Sound
   

   @classmethod
   def list():
      '''Creates an empty sound list that can contain several sounds.
         
         Arguments:
         @random (int): whether the playback will be random or not.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   @classmethod
   def sawtooth(frequency, rate=48000):
      '''Creates a sawtooth sound which plays a sawtooth wave.
         
         Arguments:
         @frequency (float): The frequency of the sawtooth wave in Hz.
         @rate (int): The sampling rate in Hz. It's recommended to set thisvalue to the playback device's samling rate to avoid resamping.
         
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   @classmethod
   def silence(rate=48000):
      '''Creates a silence sound which plays simple silence.
         
         Arguments:
         @rate (int): The sampling rate in Hz. It's recommended to set thisvalue to the playback device's samling rate to avoid resamping.
         
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   @classmethod
   def sine(frequency, rate=48000):
      '''Creates a sine sound which plays a sine wave.
         
         Arguments:
         @frequency (float): The frequency of the sine wave in Hz.
         @rate (int): The sampling rate in Hz. It's recommended to set thisvalue to the playback device's samling rate to avoid resamping.
         
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   @classmethod
   def square(frequency, rate=48000):
      '''Creates a square sound which plays a square wave.
         
         Arguments:
         @frequency (float): The frequency of the square wave in Hz.
         @rate (int): The sampling rate in Hz. It's recommended to set thisvalue to the playback device's samling rate to avoid resamping.
         
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   @classmethod
   def triangle(frequency, rate=48000):
      '''Creates a triangle sound which plays a triangle wave.
         
         Arguments:
         @frequency (float): The frequency of the triangle wave in Hz.
         @rate (int): The sampling rate in Hz. It's recommended to set thisvalue to the playback device's samling rate to avoid resamping.
         
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def ADSR(attack, decay, sustain, release):
      '''Attack-Decay-Sustain-Release envelopes the volume of a sound.
         Note: there is currently no way to trigger the release with this API.
         
         Arguments:
         @attack (float): The attack time in seconds.
         @decay (float): The decay time in seconds.
         @sustain (float): The sustain level.
         @release (float): The release level.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def accumulate(additive=False):
      '''Accumulates a sound by summing over positive input
         differences thus generating a monotonic sigal.
         If additivity is set to true negative input differences get added too,
         but positive ones with a factor of two.
         Note that with additivity the signal is not monotonic anymore.
         
         Arguments:
         @additive: Whether the accumulation should be additive or not.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def addSound(sound):
      '''Adds a new sound to a sound list.
         
         Arguments:
         @sound (Sound): The sound that will be added to the list.
   
         Note: You can only add a sound to a sound list.
      '''
   
      pass
   

   def cache():
      '''Caches a sound into RAM.
         This saves CPU usage needed for decoding and file access if the
         underlying sound reads from a file on the harddisk,
         but it consumes a lot of memory.
         
         @returns (Sound): The created Sound object.
         Note: Only known-length factories can be buffered... warning::
         Raw PCM data needs a lot of space, only buffer
         short factories.
         
      '''
   
      return Sound
   

   def data():
      '''Retrieves the data of the sound as numpy array.
         
         @returns (numpy.ndarray): A two dimensional numpy float array.
         Note: Best efficiency with cached sounds.
      '''
   
      return numpy.ndarray
   

   def delay(time):
      '''Delays by playing adding silence in front of the other sound's data.
         
         Arguments:
         @time (float): How many seconds of silence should be added before the sound.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def envelope(attack, release, threshold, arthreshold):
      '''Delays by playing adding silence in front of the other sound's data.
         
         Arguments:
         @attack (float): The attack factor.
         @release (float): The release factor.
         @threshold (float): The general threshold value.
         @arthreshold (float): The attack/release threshold value.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def fadein(start, length):
      '''Fades a sound in by raising the volume linearly in the given
         time interval.
         
         Arguments:
         @start (float): Time in seconds when the fading should start.
         @length (float): Time in seconds how long the fading should last.
   
         @returns (Sound): The created Sound object.
         Note: Before the fade starts it plays silence.
      '''
   
      return Sound
   

   def fadeout(start, length):
      '''Fades a sound in by lowering the volume linearly in the given
         time interval.
         
         Arguments:
         @start (float): Time in seconds when the fading should start.
         @length (float): Time in seconds how long the fading should last.
   
         @returns (Sound): The created Sound object... note::
         After the fade this sound plays silence, so that
         the length of the sound is not altered.
         
      '''
   
      return Sound
   

   def filter(b, a = (1)):
      '''Filters a sound with the supplied IIR filter coefficients.
         Without the second parameter you'll get a FIR filter.
         If the first value of the a sequence is 0,
         it will be set to 1 automatically.
         If the first value of the a sequence is neither 0 nor 1, all
         filter coefficients will be scaled by this value so that it is 1
         in the end, you don't have to scale yourself.
         
         Arguments:
         @b (sequence of float): The nominator filter coefficients.
         @a (sequence of float): The denominator filter coefficients.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def highpass(frequency, Q=0.5):
      '''Creates a second order highpass filter based on the transfer
         function :math:H(s) = s^2 / (s^2 + s/Q + 1)
         
         Arguments:
         @frequency (float): The cut off trequency of the highpass.
         @Q (float): Q factor of the lowpass.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def join(sound):
      '''Plays two factories in sequence.
         
         Arguments:
         @sound (Sound): The sound to play second.
   
         @returns (Sound): The created Sound object... note::
         The two factories have to have the same specifications
         (channels and samplerate).
         
      '''
   
      return Sound
   

   def limit(start, end):
      '''Limits a sound within a specific start and end time.
         
         Arguments:
         @start (float): Start time in seconds.
         @end (float): End time in seconds.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def loop(count):
      '''Loops a sound.
         
         Arguments:
         @count (integer): How often the sound should be looped.Negative values mean endlessly.
         
   
         @returns (Sound): The created Sound object... note::
         This is a filter function, you might consider using
         :attr:Handle.loop_count instead.
         
      '''
   
      return Sound
   

   def lowpass(frequency, Q=0.5):
      '''Creates a second order lowpass filter based on the transfer    function :math:H(s) = 1 / (s^2 + s/Q + 1)
         
         Arguments:
         @frequency (float): The cut off trequency of the lowpass.
         @Q (float): Q factor of the lowpass.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def mix(sound):
      '''Mixes two factories.
         
         Arguments:
         @sound (Sound): The sound to mix over the other.
   
         @returns (Sound): The created Sound object... note::
         The two factories have to have the same specifications
         (channels and samplerate).
         
      '''
   
      return Sound
   

   def modulate(sound):
      '''Modulates two factories.
         
         Arguments:
         @sound (Sound): The sound to modulate over the other.
   
         @returns (Sound): The created Sound object... note::
         The two factories have to have the same specifications
         (channels and samplerate).
         
      '''
   
      return Sound
   

   def mutable():
      '''Creates a sound that will be restarted when sought backwards.
         If the original sound is a sound list, the playing sound can change.
         
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def pingpong():
      '''Plays a sound forward and then backward.
         This is like joining a sound with its reverse.
         
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def pitch(factor):
      '''Changes the pitch of a sound with a specific factor.
         
         Arguments:
         @factor (float): The factor to change the pitch with.
   
         @returns (Sound): The created Sound object... note::
         This is done by changing the sample rate of the
         underlying sound, which has to be an integer, so the factor
         value rounded and the factor may not be 100 % accurate.
         .. note::
         This is a filter function, you might consider using
         :attr:Handle.pitch instead.
         
      '''
   
      return Sound
   

   def rechannel(channels):
      '''Rechannels the sound.
         
         Arguments:
         @channels (int): The new channel configuration.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def resample(rate, high_quality):
      '''Resamples the sound.
         
         Arguments:
         @rate (double): The new sample rate.
         @high_quality (bool): When true use a higher quality but slower resampler.
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def reverse():
      '''Plays a sound reversed.
         
         @returns (Sound): The created Sound object... note::
         The sound has to have a finite length and has to be seekable.
         It's recommended to use this only with factories with
         fast and accurate seeking, which is not true for encoded audio
         files, such ones should be buffered using :meth:cache before
         being played reversed.
         .. warning::
         If seeking is not accurate in the underlying sound
         you'll likely hear skips/jumps/cracks.
         
      '''
   
      return Sound
   

   def sum():
      '''Sums the samples of a sound.
         
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def threshold(threshold = 0):
      '''Makes a threshold wave out of an audio wave by setting all samples
         with a amplitude >= threshold to 1, all <= -threshold to -1 and
         all between to 0.
         
         Arguments:
         @threshold (float): Threshold value over which an amplitude countsnon-zero.
         
   
         @returns (Sound): The created Sound object.
      '''
   
      return Sound
   

   def volume(volume):
      '''Changes the volume of a sound.
         
         Arguments:
         @volume (float): The new volume..
   
         @returns (Sound): The created Sound object.
         Note: Should be in the range [0, 1] to avoid clipping... note::
         This is a filter function, you might consider using
         :attr:Handle.volume instead.
         
      '''
   
      return Sound
   

   def write(filename, rate, channels, format, container, codec, bitrate, buffersize):
      '''Writes the sound to a file.
         
         Arguments:
         @filename (string): The path to write to.
         @rate (int): The sample rate to write with.
         @channels (int): The number of channels to write with.
         @format (int): The sample format to write with.
         @container (int): The container format for the file.
         @codec (int): The codec to use in the file.
         @bitrate (int): The bitrate to write with.
         @buffersize (int): The size of the writing buffer.
   
      '''
   
      pass
   

   length = None
   '''The sample specification of the sound as a tuple with rate and channel count.
      
   '''
   

   specs = None
   '''The sample specification of the sound as a tuple with rate and channel count.
      
   '''
   



class Source:
   '''The source object represents the source position of a binaural sound.
      
   '''

   azimuth = None
   '''The azimuth angle.
      
   '''
   

   distance = None
   '''The distance value. 0 is min, 1 is max.
      
   '''
   

   elevation = None
   '''The elevation angle.
      
   '''
   



class ThreadPool:
   '''A ThreadPool is used to parallelize convolution efficiently.
      
   '''



class error:
   



