
Uma das alternativas para coletar as informações disponíveis na web (notícias, fórum, comentários, etc) são os  **Web crawlers**. De maneira resumida, um  **Web crawler**  é um programa que  **colhe conteúdo na web**  de forma sistematizada através do protocolo padrão da web (http/https).

[**Rastreador web - Wikipédia, a enciclopédia livre** ](https://pt.wikipedia.org/wiki/Rastreador_web "https://pt.wikipedia.org/wiki/Rastreador_web")


Como os Web crawlers não dependem de API específica,  **tudo**  que está disponível na internet se torna passível de ser  **colhida**.

> Se está na internet, é ~~verdade~~ coletável

Dessa forma, técnicas de Web crawlers são bastante utilizadas para  **diversos propósitos**:

-   **Motores de busca**
-   **Monitoramento de marcas** ou assuntos em portais e notícias
-   Criação de  **banco de dados offline**  para processamento de conteúdo originalmente na web (imagens, vídeos, text, etc)

A maioria das linguagens de programação dão suporte a ferramentas que possibilitam a realização de Web Crawler, existem também bibliotecas específicas, como o  [**Scrapy**](http://scrapy.org/)  em Python, o  [**crawler4j**](https://github.com/yasserg/crawler4j)  em Java, e o  [**Mechanize**](https://github.com/sparklemotion/mechanize)  e  [**Watir**](http://watir.com/)  que são bibliotecas Ruby.

Nesse mini-curso utilizaremos o  **Scrapy**  para coletar notícias, criando assim um crawler que pode ser utilizado para monitoramento de assuntos em sites de notícias.

[**Scrapy | A Fast and Powerful Scraping and Web Crawling Framework** ](https://scrapy.org/)

----------

### Scrapy, o que é?

> **Scrapy** é um  **Framework**  open source para  **extração**  de informação em websites, ou seja, Framework para  **Web Crawler**.

![](https://cdn-images-1.medium.com/max/1200/0*qMPp45e8UUEuBeJE.png)

Por ser um  **Framework**, o Scrapy disponibiliza diversas funcionalidades que facilitam o o processo de crawler. Desde o controle de navegação na web, bibliotecas de parse em HTML, representação de dados e pipelines para filtragem e tratamento de dados.

#### Instalando e criando projeto com Scrapy

O Scrapy é um pacote do Python e está disponível pelo  [_pip_](https://pypi.python.org/pypi/pip)_._ Pra instalar a última versão do Scrapy pelo  `pip` o comando é :

_$ pip install scrapy_

Após a instalação, já é possível criar um projeto Scrapy com o comando:

_$ scrapy startproject_ **_MEU_PROJETO_**

Um projeto Scrapy é composto por alguns arquivos e diretórios que estão relacionados com o fluxo de crawler pelo Framework.

![](https://cdn-images-1.medium.com/max/1600/1*nu27VuJSMsaESfG5leTEPA.png)

#### Estrutura de pastas de um projeto Scrapy

-   Na pasta **_'/../spiders'_** ficam os arquivos de  _spiders,_  onde são definidos os sites que serão utilizados no crawler, o fluxo de navegação nesses sites e como será feito o parse no  _html_  para extração da informação do crawler.
-   No arquivo  **_‘Items.py’_**  são definidos as classes de representação da informação. Essa é uma maneira de padronizar a informação que está sendo colhida pelo crawler. Dessa forma, mesmo usando  _spiders_ diferentes (páginas diferentes), é possível padronizar o item que está sendo colhido.
-   No arquivo  **_‘middlewares.py’_** é definido como a resposta http será processada e enviada para o  _spider._ Geralmente não é necessário modificar o  _middleware_  padrão do Scrapy, mas a depender do site que o  _crawler_  será realizado e da complexidade se torna necessário customizar o  _middleware_.
-   No arquivo ‘**_pipelines.py’_** são definidos os  _pipelines_  para processamento de cada Item. Ou seja, após o  _spider_  colher o  _item,_ o item passa por um o mais pipelines em sequência para que seja realizada alguma operação limpeza de dados, validação do item, checagem de duplicidade e se salvamento do item em um arquivo ou banco de dados.
-   No arquivo  **_‘settings.py’_** está a configuração do projeto Scrapy. Nesse arquivo é possível definir a ordem de execução dos  _pipelines,_ qual middleware está habilitado, entre outras configurações.
-   O arquivo  **_‘scrapy.cfg’_** é define algumas variáveis do projeto.

A documentação do Scrapy é bem completa. Demais informações podem ser encontradas em:

[**Scrapy 1.5 documentation** ](https://docs.scrapy.org/en/latest/)

----------

### Utilizando o Scrapy para coletar notícias

Uma das utilizações de **Web crawler**  é o monitoramento de informações em sites de notícias. Dessa forma, colher as notícias é o primeiro passo para qualquer análise.

Iremos utilizar o  **Scrapy**  para coletar as notícias do site  **Tecnoblog**, um dos maiores portais brasileiros voltado a notícias de tecnologia.

[**Tecnoblog** ](https://tecnoblog.net/)

----------

#### Criando o Projeto

    $ scrapy startproject noticias  
    $ cd noticias

Dentro da pasta de um projeto Scrapy é possível executar alguns comandos específicos ao projeto, como criar spiders, executar o crawler.. etc

#### Spider

Após criar o projeto o primeiro passo é criar um  _spider_  para coletar os dados:

`$ scrapy genspider Tecnoblog tecnoblog.net`

O  _spider_  é responsável pelo site que será realizado o Crawler, pelo fluxo de navegação e pelo  _parse_  _html_  para extração de informação. A estrutura básica de um  _spider_  é a seguinte:



O  _crawler_  começa na URL  [_http://tecnoblog.net_,](http://tecnoblog.net%2C/)  que é a index com as notícias do Tecnoblog. O  **_start_urls_**  pode ser definido com mais de um elemento, ou seja, sites que tem urls diferentes por categoria de notícias (esportes, economia, tecnologia.. etc.), mas compartilham a mesma estrutura do html para que o parse seja igual.

A função de  **_parse_**_(self, response)_ recebe a resposta da requisição (_response)_, que no caso é o HTML, e realiza o  _parse_  para extração da informação que está sendo colhida.

Antes de fazer a função de  **parse**, é interessante usar algum  _inspector_ de elemento html (famoso _Inspect_ do **chrome**  )  e o  **_shell_** _do_ **Scrapy**  para “brincar” de buscar a informação de forma  **interativa**.

    $ scrapy shell http://tecnoblog.net

![](https://cdn-images-1.medium.com/max/1600/1*HeY-38S5g9OBV49lc4G81g.gif)

O scrapy utiliza diferentes bibliotecas que podem ser utilizadas para realizar o  _parse_  no html, os chamados seletores podem ser melhor explicados em [Selectors - Scrapy 1.4.0 documentation](https://doc.scrapy.org/en/latest/topics/selectors.html)

Depois de “brincar” com a  _shell_  do scrapy e descobrir como coletar as informações necessárias, a função de  `parse`  do spider pode ser modificada para:


```python
# -*- coding: utf-8 -*-

import scrapy
from noticias.items import NoticiasItem

class TecnoblogSpider(scrapy.Spider):
    name = 'Tecnoblog'
    allowed_domains = ['tecnoblog.net']
    start_urls = ['https://tecnoblog.net/']

    def parse(self, response):
	    link = article.css("div.texts h2 a::attr(href)").extract_first()
	    title = article.css("div.texts h2 a::text").extract_first()
		author = article.css("div.texts div.info a::text").extract_first()
		
		notice = NoticiasItem(title=title, author=author, link=link)

		yield notice
```

Dessa forma, utilizando a página inicial do  [_http://tecnoblog.net_](http://tecnoblog.net%2C/), é possível coletar as informações de  **titulo**,  **autor**  e  **link**  da notícia. O retorno da função de  `_parse_`  com a  `_yield_`  pode ser um  `Json`  ou um  **Item**  do Scrapy.

Em um projeto Scrapy podem existir diferentes  _spiders_, em que cada  _spider_  é referente a uma fonte de crawler. Por exemplo, em nosso caso de  _crawler_  em portais de notícias, além do spider criado para o  [_Tecnoblog_](http://tecnoblog.net%2C/)_, podemos criar spiders para o G1,_ [_Techtudo_](http://www.techtudo.com.br/) _ou_  qualquer outro site de notícias, ao retornar sempre um objeto do mesmo tipo, deixamos a parte de pipelines independente do crawler.

O  _spider_  pode ser executado em standalone ou pelo framework com os demais  _spiders_. Para executar apenas o spyper em desenvolvimento o comando é o  `runspider`

`$ scrapy runspider noticias/spiders/Tecnoblog.py`

----------

#### Item

No arquivo  `items.py` é possível definir a estrutura da informação que espera coletar com o crawler. Dessa forma é possível criar uma classe que representa essa informação, com atributos e métodos se necessário. Para o nosso caso, uma representação de uma notícias pode ser da seguinte forma:
```python
import scrapy

class NoticiasItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()
```

Além de padronizar a informação do crawler, a utilização do  `Item`  facilita os demais métodos do framework.

----------

#### Fluxo de Navegação

Quando falamos de fluxo de navegação de um crawler, estamos falando das páginas e sub-páginas que a  **_spider_**  deve visitar para colher a informação por completo. Embora realizar o  **crawler**  na  **página inicial**  traga resultados, nem sempre tem toda a informação da notícia ou mesmo todas as notícias. Para esses casos são necessários os fluxos de navegação.

O Spider pode  _seguir links_  nas páginas, da mesma forma que uma pessoa faria ao acessar o site de notícias e se deparar com a página inicial:

-   Acessa a  **página específica da notícias**  para coletar todas as informações, em vez de usar apenas a página de listagem.
-   Busca a opção de “Mais notícias” ou os “links de 1,2,3,4…30 página” que redirecionam a navegação para uma **nova página com estrutura igual e noticias ainda não colhidas**.

```python
import scrapy
from noticias.items import NoticiasItem

class TecnoblogSpider(scrapy.Spider):
	name = 'Tecnoblog'
	allowed_domains = ['tecnoblog.net']
	start_urls = ['http://tecnoblog.net/']

	def parse(self, response):
		for article in response.css("article"):
			link = article.css("div.texts h2 a::attr(href)").extract_first()
			yield response.follow(link, self.parse_article)
	
	def parse_article(self, response):
		link = response.url
		title = response.css("title ::text").extract_first()
		author = response.css("span.author ::text").extract_first()
		text = "".join(response.css("div.entry ::text").extract())

		notice = NoticiasItem(title=title, author=author, text=text, link=link)

		yield notice
```

—  **Página especifica da notícia**

No Spider podemos mudar o fluxo de navegação com a função  **_follow,_** dessa forma colhemos a informação dentro da página específica da notícia. Geralmente a página de exibição da notícias requer um  _parse_  diferente, nesse caso é necessário criar uma nova função de  _parse_ (o shell do scrapy pode ajudar).

Assim o  `response.follow(link, parse_article)`  “entra” na pagina especifica da notícia e faz o  _parse_  com a função  `parse_article`. O retorno continua sendo a nossa estrutura de notícia.

**— “Mais Notícias”**

A depender da necessidade do crawler se torna necessário visitar todas as páginas do site. Se o objetivo for coletar apenas as  **últimas notícias**, a página inicial é suficiente, mas se o objetivo for  **coletar TODAS**  as notícias do site, será necessário fazer um fluxo que visite todas as páginas.

O primeiro passo é identificar os botões de “Mais Páginas”, “Numeração de Páginas” ou outros links que levem as demais páginas de notícias do site. Dessa forma é possível forçar o fluxo a percorrer todas as páginas ao localizar o link de “Mais Páginas”.

É importante que as demais páginas sigam a mesma estrutura do html, dessa forma a função de  _parse_  é a mesma e pode ser utilizada de forma recursiva.

O fluxo no Spider pode ser alterado para:

**Cuidado!**  A depender de como a recursão é feita, além de demorar MUITO, o fluxo pode ficar preso. Geralmente se utiliza um limitador de quantidade de redirecionamentos ou itens coletados quando não for o objetivo coletar TODO o site.

----------

#### Pipeline

No arquivo ‘**_pipelines.py’_** são definidos os  _pipelines._ Essa parte é independente do crawler e tem como principal objetivo responder a pergunta:

> O que fazer com os Itens colhidos no crawler?

A resposta depende da aplicação, mas de modo geral sempre tem a ver com filtragem da informação, alteração ou limpeza e armazenamento da informação.

Um pipeline contem alguns métodos. Os métodos de  `open_sipder`  e  `close_spider`  são executados apenas uma vez, quando o spider é iniciado e quando o spider termina. Geralmente essas duas funções são utilizadas para abrir e fechar conexões com banco de dados ou arquivos.

O método  `process_item`  é executado sempre que o  _spider_  retorna um item encontrado no crawler, ou seja, para o nosso exemplo a cada notícia coletada. No método  `process_item`  que deve ser executado a filtragem, alteração ou salvamento do item no banco de dados.

**— Dropando o item**

No caso de querer dropar uma reportagem que tem tem autor:

```python
def process_item(self, item, spider):
	if item['author']:
		return item
	else:
		raise DropItem("Sem autor no item {}".format(item))

return item
```

**— Alterando o item**

Para que o autor seja colocado como upcase:
```python
def process_item(self, item, spider):
	item['author'] = item['author'].upper()
	return item
```

**— Salvando o item em um arquivo**

Para salvar o item em um arquivo `‘notices.txt’`, nesse exemplo usamos a função de  `open_spider`  para abrir o arquivo, a  `process_item`  para salvar no arquivo e a  `close_spider`  para fechar o fluxo.
```python
import json

class NoticiasPipeline(object):
	def open_spider(self, spider):
		self.file = open('notices.txt', 'w')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
      line =  json.dumps(dict(item), ensure_ascii=False).encode('utf8') + '\n'
      self.file.write(line)
      return item
```

Diferentes pipelines podem ser empilhados, ou seja, podemos ter um pipeline para  **realizar a filtragem**  (decidir se o item é importante), outro para  **limpar a informação**  (retirando tags html se necessário) e por último um pipeline para  **salvar a informação no banco de dados**. Dessa forma os três exemplos anteriores podem estar em pipelines diferentes.

A ordem de execução dos pipelines é definida no arquivo de configuração do Scrapy,  `‘settings.py’`

## Concluindo
A framework **_Scrapy_** é sem dúvida a ferramenta Python mais prática e completa da comunidade. Com métodos simples e várias facilidades, qualquer programador curioso com estudo e prática é possivel fazer coisas gigantes.
O projeto completo  utilizado durante o mini-curso está disponivel no meu [GitHub](https://github.com/VGasparini/minicurso-scrapping)
