from database.conexion import init_db
from database.seed import seed_data

from app import App


init_db()
seed_data()

app = App()
app.mainloop()