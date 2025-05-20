class AuthServer:
    def authenticate(self, username, password):
        if username == "user" and password == "pass":
            return True
        return False


class ContentServer:
    def get_movie_list(self):
        return ["Inception", "The Matrix", "Interstellar"]

    def stream_movie(self, movie):
        return f"Streaming '{movie}' now..."


class NetflixApp:
    def __init__(self):
        self.auth_server = AuthServer()
        self.content_server = ContentServer()
        self.logged_in = False

    def start_app(self):
        print("넷플릭스 앱을 실행합니다.")

    def login(self, username, password):
        print("로그인 시도 중...")
        self.logged_in = self.auth_server.authenticate(username, password)
        if self.logged_in:
            print("로그인 성공! 홈 화면을 표시합니다.")
        else:
            print("로그인 실패. 앱을 종료합니다.")

    def browse_content(self):
        if not self.logged_in:
            print("로그인 후 이용 가능합니다.")
            return
        print("영화 목록을 불러옵니다...")
        movies = self.content_server.get_movie_list()
        print("영화 목록:", movies)

    def watch_movie(self, movie):
        if not self.logged_in:
            print("로그인 후 이용 가능합니다.")
            return
        print(f"'{movie}' 재생 요청 중...")
        stream = self.content_server.stream_movie(movie)
        print(stream)


# 실행 예시
if __name__ == "__main__":
    app = NetflixApp()
    app.start_app()
    app.login("user", "pass")           # 로그인 성공
    app.browse_content()                # 영화 탐색
    app.watch_movie("Inception")        # 영화 재생
