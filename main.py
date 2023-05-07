from pydub import AudioSegment
import os


def rip_cd(source_path, target_path):
    # Crea una lista de archivos WAV para guardar los fragmentos de audio del CD
    track_list = []

    for i, track in enumerate(AudioSegment.from_wav(source_path)):
        # Guarda la pista como un archivo WAV en la carpeta de destino
        track.export(os.path.join(target_path, f"track{i}.wav"), format="wav")

        track_list.append(f"track{i}.wav")

    return track_list

source_path = "/dev/cdrom"
target_path = "/home/user/cd_tracks"
track_list = rip_cd(source_path, target_path)

# Imprime la lista de archivos de pista
print(track_list)
