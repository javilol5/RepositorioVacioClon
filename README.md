# Clonacion

# Desafío Git: Flujo de Trabajo Híbrido (Clonado y Remotos)

## Preguntas y Respuestas

---

### 1. ¿Cómo se hace desde el PyCharm? (para *Clonar el Repositorio del Compañero*)

**Respuesta:**
En PyCharm puedes clonar un repositorio siguiendo estos pasos:
1. Abre PyCharm.  
2. Ve a **File → New → Project from Version Control → Git**.  
3. En el campo **URL**, pega la dirección del repositorio del compañero.  
4. Elige el directorio donde se guardará el proyecto local.  
5. Haz clic en **Clone**.  
PyCharm descargará el repositorio y lo abrirá automáticamente.

---

### 2. ¿Cómo se hace desde el PyCharm? (para *Configurar el Usuario Local*)

**Respuesta:**
Para configurar el usuario local en PyCharm:
1. Abre el menú superior **File → Settings → Version Control → Git** (en macOS: **PyCharm → Preferences → Version Control → Git**).  
2. En la sección **Commit**, selecciona la pestaña **Commit Author** o **User Name and Email**.  
3. Escribe tu nombre y correo electrónico en los campos correspondientes.  
4. Guarda los cambios.  
También puedes hacerlo desde la terminal integrada de PyCharm con los mismos comandos:  
```bash
  git config user.name "Tu Nombre"
  git config user.email "tu.email@ejemplo.com"
```

---

### 3. ¿Cómo se hace desde el PyCharm? (para *Ver Repositorios Remotos Actuales*)

**Respuesta:**
En PyCharm:
1. Abre el menú **VCS → Git → Remotes…**.  
2. Se abrirá una ventana con la lista de repositorios remotos configurados.  
3. Deberías ver solo **origin** con sus URLs de *fetch* y *push*.  
También puedes abrir la terminal integrada y escribir:  
```bash
  git remote -v
```

---

### 4. ¿Cómo se hace desde el PyCharm? (para *Añadir el Repositorio Personal como Nuevo Remoto*)

**Respuesta:**
En PyCharm:
1. Ve al menú **VCS → Git → Remotes…**.  
2. Haz clic en el botón **+ (Add)**.  
3. En el campo **Name**, escribe `mirepositorio`.  
4. En el campo **URL**, pega la dirección del nuevo repositorio de GitHub.  
5. Haz clic en **OK**.  
Desde la terminal también podrías hacerlo con:  
```bash
  git remote add mirepositorio URL_de_tu_nuevo_repositorio
```

---

### 5. ¿Cómo se hace desde el PyCharm? (para *Eliminar el Remoto Original*)

**Respuesta:**
En PyCharm:
1. Abre **VCS → Git → Remotes…**.  
2. Selecciona el remoto **origin**.  
3. Haz clic en el botón **– (Remove)** y confirma.  
Alternativamente, en la terminal integrada:  
```bash
  git remote remove origin
```

---

### 6. ¿Cómo se hace desde el PyCharm? (para *Ver Repositorios Remotos Finales*)

**Respuesta:**
En PyCharm:
1. Abre nuevamente **VCS → Git → Remotes…**.  
2. Comprueba que solo aparece **mirepositorio**.  
O desde la terminal:  
```bash
  git remote -v
```
Debe mostrar únicamente las URLs asociadas a `mirepositorio`.

---

### 7. ¿Cómo se hace desde la terminal? (para *Add y Commit*)

**Respuesta:**
En la terminal (dentro del repositorio):
1. Verifica los archivos modificados:
   ```bash
   git status
   ```
2. Añade los cambios al área de preparación:
   ```bash
   git add main.py
   ```
3. Realiza el commit con un mensaje descriptivo:
   ```bash
   git commit -m "Añadida la primera modificación del alumno"
   ```
Esto equivale al proceso gráfico de PyCharm (seleccionar archivo → escribir mensaje → Commit).

Foto mostrando los 2 repositorios remotos finales en github:

![Ambos repositorios en github](/media/foto%20repositorios.png)