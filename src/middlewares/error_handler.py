from starlette.middleware.base import BaseHTTPMiddleware #Necesito este módulo par mi clase error handler
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

# Clse que maneja los errores
class ErrorHandler(BaseHTTPMiddleware):
    # Método constructtor, requiere de una plicación, que diré que es de tipo FastAPI, por ello lo importo
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)# Le envío la aplicación al método super

    #Función asíncrona que se va a ejecutar si ocurre un error en nuestra aplicación (método dispatch)
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
    # Requiere un parámetro request para acceder a las peticiones que llegan a la aplicación, call next llama a la siguente función en caso de que no suceda ningún error.
    # En caso de que no ocurra un error devolvemos una respuesta (response) ye n caso de que haya error, damos un Json response
        try:
            return await call_next(request)
            # Si no ocurre error se llama a la siguente función. como es asíncrona hay que añadir await
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})
            # Envío un mensaje de error