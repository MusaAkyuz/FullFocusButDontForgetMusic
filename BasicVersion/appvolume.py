from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from pycaw.constants import AudioSessionState
from pycaw.magic import MagicApp

def handle_all(*args):
    print("callback")
    print(args)


# Find the target application by its name
target_app_names = ["msedge.exe", "chrome.exe", "WhatsApp.exe"]
spotify_app_name = "Spotify.exe"

spotify = MagicApp(
    {"Spotify.exe"},
    volume_callback=handle_all,
    mute_callback=handle_all,
    state_callback=handle_all,
    session_callback=handle_all,
)

while True:

    sessions = AudioUtilities.GetAllSessions()
    any_target_app_is_playing = False

    for session in sessions:
        if session.Process and session.Process.name() in target_app_names:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            is_sound = session.State == AudioSessionState.Active
            if is_sound:
                any_target_app_is_playing = True
                break
            else:
                any_target_app_is_playing = False

    if not any_target_app_is_playing:
        if spotify.state:
            spotify.volume = 0.99
    else:
        if spotify.state:
            spotify.volume = 0.3