import os

path = "tools\\ffmpeg.exe"

def launch(inputs, output, options="", outputOptions="") -> str:
    command = path
    command += " " + options 
    for input, inputOptions in inputs.items():
        if inputOptions:
            command += " " + inputOptions
        command += " -i " + input
    if outputOptions:
        command += " " + outputOptions
    command += " " + output
    os.system(command)
    return command
