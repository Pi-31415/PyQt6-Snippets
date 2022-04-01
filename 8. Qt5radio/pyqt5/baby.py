import sys
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import Gst, GstVideo
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QOpenGLWidget, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initPlayer()

    def initUI(self):
        self.setWindowTitle('Ogg-Player')
        self.resize(546, 475)
        self.setGeometry(0, 0, 546, 475)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.openGLWidget = QOpenGLWidget(self)

        self.button = QPushButton(self)
        self.button.setText('Start')
        self.button.clicked.connect(self.start_stop)

        self.verticalLayout.addWidget(self.openGLWidget)
        self.verticalLayout.addWidget(self.button)

        self.show()

    def initPlayer(self):
        Gst.init(None)
        self.player = Gst.Pipeline.new("player")
        source = Gst.ElementFactory.make("filesrc", "file-source")
        demuxer = Gst.ElementFactory.make("oggdemux", "demuxer")
        demuxer.connect("pad-added", self.demuxer_callback)

        self.queuea = Gst.ElementFactory.make("queue", "queuea")
        self.queuev = Gst.ElementFactory.make("queue", "queuev")

        self.audio_decoder = Gst.ElementFactory.make("vorbisdec", "vorbis-decoder")
        audioconv = Gst.ElementFactory.make("audioconvert", "convertera")
        audiosink = Gst.ElementFactory.make("autoaudiosink", "audio-output")

        self.video_decoder = Gst.ElementFactory.make("theoradec", "theora-decoder")
        videoconv = Gst.ElementFactory.make("videoconvert", "converterv")
        videosink = Gst.ElementFactory.make("autovideosink", "video-output")

        self.player.add(source)
        self.player.add(demuxer)
        self.player.add(self.audio_decoder)
        self.player.add(audioconv)
        self.player.add(audiosink)
        self.player.add(self.queuea)

        self.player.add(self.video_decoder)
        self.player.add(videoconv)
        self.player.add(videosink)
        self.player.add(self.queuev)

        source.link(demuxer)
        self.queuea.link(self.audio_decoder)
        self.audio_decoder.link(audioconv)
        audioconv.link(audiosink)

        self.queuev.link(self.video_decoder)
        self.video_decoder.link(videoconv)
        videoconv.link(videosink)

        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.connect('message', self.on_message)
        bus.enable_sync_message_emission()
        bus.connect("sync-message::element", self.on_sync_message)

    def start_stop(self):
         if self.button.text() == 'Start':
             filepath = QFileDialog.getOpenFileName(self,"Choose a file!", "","Ogg Files (*.ogg)")
             #filepath returns a tuple containing ('/home/yourpathhere/yourfilenamehere.ogg', 'Ogg Files (*.ogg)')
             #we need to unpack this tuple to obtain a filename we can use
             #filepath[0] is a string containing the filename we want for example /home/yourpathhere/yourfilenamehere.ogg
             if filepath:
                 self.button.setText('Stop')
                 self.player.get_by_name("file-source").set_property("location", filepath[0])
                 self.player.set_state(Gst.State.PLAYING)
         else:
             self.player.set_state(Gst.State.NULL)
             self.button.setText('Start')

    def demuxer_callback(self, demuxer, newpad):
        res = Gst.Pad.get_current_caps(newpad)
        structure = Gst.Caps.get_structure(res, 0)
        result = Gst.Structure.get_name(structure)
        if "audio" in result:
            print(result)
            adec_pad = self.queuea.get_static_pad("sink")
            newpad.link(adec_pad)
        if "video" in result:
            vdec_pad = self.queuev.get_static_pad("sink")
            newpad.link(vdec_pad)

    def on_message(self, bus, message):
         t = message.type
         if t == Gst.MessageType.EOS:
             self.player.set_state(Gst.State.NULL)
             self.button.setText('Start')
         elif t == Gst.MessageType.ERROR:
             self.player.set_state(Gst.State.NULL)
             err, debug = message.parse_error()
             print('Error: %s' % err, debug)
             self.button.setText('Start')

    def on_sync_message(self, bus, message):
        if message.get_structure().get_name() == 'prepare-window-handle':
            videosink = message.src
            videosink.set_property("force-aspect-ratio", True)
            videosink.set_window_handle(self.openGLWidget.winId())


if __name__ == '__main__':

     qApp = QApplication(sys.argv)
     MainWindow()
     sys.exit(qApp.exec_())
