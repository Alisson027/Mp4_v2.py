from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

KV = '''
FloatLayout:

    Image:
        source: 'Download.jpeg'
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDScreen:
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(20)

            MDTextField:
                id: url_input
                hint_text: "Digite o URL"
                helper_text: "Insira o URL do vídeo"
                helper_text_mode: "on_focus"

            MDRaisedButton:
                text: "Baixar"
                on_release: app.download_button_click(url_input.text)
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def download_button_click(self, url):
        try:
            # Importa o back-end
            from mp4_v2 import download_video

            # Chama a função de download do back-end
            download_video(url)
        except Exception as e:
            print(f"Erro durante o download: {e}")

MyApp().run()