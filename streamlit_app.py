
import streamlit as st
#importamos las librerias necesarias para web scraping
from newspaper import Article


def get_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article
#creamos una funcion para extraer los parrafos
def get_parrafos(text):
    #creamos un array para guardar los parrafos
    parrafos = []
    #extraemos los parrafos del articulo
    for p in text.split('\n\n'):
        parrafos.append(p)
    #retornamos los parrafos
    return parrafos
def string_authors(authors):
    #creamos un string para guardar los autores
    string_authors = ''
    #recorremos el array de autores
    for author in authors:
        #si solo hay un autor
        if len(authors) == 1:
            #retornamos el autor
            return author
        else:
            #concatenamos los autores  sin añadir la coma al final
            if author == authors[-1]:
                string_authors += author
            else:
                string_authors += author + ', '
    #retornamos el string de autores
    return string_authors
def get_date(date):
    #seleccionar solo la fecha de un objeto datetime
    date = date.date()
    #guardaren un array la fecha
    date = str(date).split('-')
    return date

def get_bibliography_apa(article):
    #obtener la fecha de publicacion
    date = get_date(article.publish_date)
    #obtener el string de autores
    authors = string_authors(article.authors)
    #obtener el titulo del articulo
    title = article.title
    #obtener el link del articulo
    link = article.url
    #crear el string de la bibliografia
    bibliography = authors + ' (' + date[0] + '). ' + title + '. Recuperado de ' + link
    return bibliography

def get_bibliography_mla(article):
    #obtener la fecha de publicacion
    date = get_date(article.publish_date)
    #obtener el string de autores
    authors = string_authors(article.authors)
    #obtener el titulo del articulo
    title = article.title
    #obtener el link del articulo
    link = article.url
    #crear el string de la bibliografia
    bibliography = authors + '. "' + title + '". ' + date[0] + ', ' + date[1] + ', ' + date[2] + '. Web. ' + date[0] + ', ' + date[1] + ', ' + date[2] + '. <' + link + '>'
    return bibliography

def get_bibliography_ieee(article):
    #obtener la fecha de publicacion
    date = get_date(article.publish_date)
    #obtener el string de autores
    authors = string_authors(article.authors)
    #obtener el titulo del articulo
    title = article.title
    #obtener el link del articulo
    link = article.url
    #crear el string de la bibliografia
    bibliography = authors + ', "' + title + '", ' + date[0] + ', ' + date[1] + ', ' + date[2] + ', ' + link
    return bibliography 

st.title('Free news extractor')
#recibimos el link de la pagina del usuario
link = st.text_input('Ingrese el link de la página web')
#usamos un boton para que el usuario pueda enviar el link
if st.button('Enviar'):
    article  = get_article(link)
    #mostramos el titulo del articulo
    st.title(article.title)
    #si el articulo tiene una fecha de publicacion
    if article.publish_date:
        date = get_date(article.publish_date)
    else:
        date = ['No disponible', 'No disponible', 'No disponible']
    #mostramos la fecha de publicacion del articulo
    st.write(date[2] + '/' + date[1] + '/' + date[0])
    #mostramos el autor del articulo
    st.write(string_authors(article.authors))
    #mostramos la imagen del articulo
    st.image(article.top_image)
    #llamamos a la funcion para extraer los parrafos
    parrafos = get_parrafos(article.text)
    #mostramos los parrafos
    for p in parrafos:
        st.write(p)
    #mostramos el link del articulo
    st.write(article.url)
    #hacer desplegable y un boton para mostrar la bibliografia
    with st.expander('Mostrar bibliografía'):
        #creamos un boton para que el usuario pueda mostrar la bibliografia
        st.subheader('Bibliografía')
        #bloeque de codigo
        st.write('APA: ' + get_bibliography_apa(article))
        st.write('MLA: ' + get_bibliography_mla(article))
        st.write('IEEE: ' + get_bibliography_ieee(article))

#hacer un pie de pagina desplegable
with st.expander('Acerca de'):
    st.write('¡En un mundo cada vez más lleno de confusión y desinformación, es más importante que nunca tener acceso a información de calidad y confiable! Pero a menudo, los grandes medios de comunicación y las agencias de noticias ponen obstáculos en forma de muros de pago para acceder a la información que necesitamos. Es por eso que hemos creado esta herramienta, para brindar una solución a esta problemática y garantizar que universitarios, investigadores y personas en general tengan acceso a la información relevante de forma gratuita. ¡Con esta herramienta, podemos luchar contra la desinformación y abrir nuevas puertas de conocimiento y oportunidades para todos!')


