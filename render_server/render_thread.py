import threading
import subprocess
import os


class RenderThread(threading.Thread):
    def __init__(self, blend_file, render_path, num, border_boolean=False, place="bl", size_multiplier=1):
        self.stdout = None
        self.stderr = None
        self.frame = num
        self.render_path = render_path
        self.blend_file = blend_file
        with open('res/sceneres.py','r') as tmp:
            render_settings = tmp.read()

        render_settings = render_settings.replace("{place}", place)
        render_settings = render_settings.replace("{border_boolean}", str(border_boolean))
        render_settings = render_settings.replace("{size_multiplier}", str(size_multiplier))

        with open("res/tmp.py", "w") as out:
            out.write(render_settings)

        threading.Thread.__init__(self)

    def run(self):
        cmd = 'blender --background {blend} -o {temp}/ -P res/tmp.py -f {num}'.format(blend=self.blend_file, temp=self.render_path, num=self.frame)
        self.p = subprocess.Popen(cmd.split(),
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

    def output(self):
        for stdout_line in iter(self.p.stdout.readline, ""):
            if len(stdout_line)>0: yield stdout_line

        for stderr_line in iter(self.p.stderr.readline, ""):
            if len(stderr_line)>0: yield stderr_line

        p.stdout.close()
        p.stderr.close()

        self.return_code = self.p.wait()

        if self.return_code:
            raise subprocess.CalledProcessError(self.return_code, cmd)

