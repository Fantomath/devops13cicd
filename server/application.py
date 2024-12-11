import http.server
import socketserver

PORT = 8000

class TestMe:
    """
    Пример класса для демонстрации тестовых методов.
    """

    def take_five(self):
        """
        Возвращает число 5.
        """
        return 5

    def port(self):
        """
        Возвращает значение порта.
        """
        return PORT

if __name__ == '__main__':
    # Создаем обработчик запросов
    Handler = http.server.SimpleHTTPRequestHandler

    # Запускаем сервер
    try:
        with socketserver.TCPServer(("", PORT), Handler) as http:
            print(f"Server running on http://0.0.0.0:{PORT}")
            http.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except OSError as e:
        print(f"Port {PORT} is already in use. Please choose another port.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Server shutting down...")
