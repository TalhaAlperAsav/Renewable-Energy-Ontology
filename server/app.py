from flask import Flask, render_template, request, redirect, url_for
from SPARQLWrapper import SPARQLWrapper, JSON


app = Flask(__name__, template_folder = 'templates', static_folder = 'static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods = ['POST','GET'])
def query():
    if request.method == 'POST':

        # Get user input from the form
        query_option = request.form.get('query_option', default = '1')

        # Select the appropriate SPARQL query based on the user's choice
        if query_option == '1':
            sparql_query = generate_query1()
            local_results = None
        elif query_option == '2':
            sparql_query = generate_query2()
            local_query = generate_local_query2()
            local_results = execute_sparql_query(local_query)
        elif query_option == '3':
            sparql_query = generate_query3()
            local_results = None
        elif query_option == '4':
            sparql_query = generate_query4()
            local_query = generate_local_query4()
            local_results = execute_sparql_query(local_query)
        elif query_option == '5':
            sparql_query = generate_query5()
            local_query = generate_local_query5()
            local_results = execute_sparql_query(local_query)
        elif query_option == '6':
            sparql_query = generate_query6()
            local_query = generate_local_query6()
            local_results = execute_sparql_query(local_query)
        elif query_option == '7':
            sparql_query = generate_query7()
            local_results = None   
        elif query_option == '8':
            sparql_query = generate_query8()
            local_results = None   
        elif query_option == '9':
            sparql_query = generate_query9()
            local_results = None 
        else:
            return render_template('index.html', error_message='Invalid query option')

        # Execute the SPARQL query
        results = execute_sparql_query(sparql_query)

        # Render the appropriate template based on the query option
        if query_option == '1':
            template_name = 'query1.html'
        elif query_option == '2':
            template_name = 'query2.html'
        elif query_option == '3':
            template_name = 'query3.html'
        elif query_option == '4':
            template_name = 'query4.html'
        elif query_option == '5':
            template_name = 'query5.html'
        elif query_option == '6':
            template_name = 'query6.html'
        elif query_option == '7':
            template_name = 'query7.html'
        elif query_option == '8':
            template_name = 'query8.html'
        else:
            template_name = 'query9.html'

        return render_template(template_name, results=results, local_results=local_results, query_option=query_option)
     
    else:
        return redirect(url_for('index'))


def execute_sparql_query(query):
    sparql = SPARQLWrapper('http://localhost:3030/ds/query')
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()['results']['bindings']

def generate_query1():
    return """
        # First SPARQL Query
        PREFIX re: <http://www.w3.org/2000/10/swap/reason#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <http://schema.org/>
        PREFIX wikibase: <http://wikiba.se/ontology#>
        PREFIX bd: <http://www.bigdata.com/rdf#>
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>

        SELECT DISTINCT ?superclass ?superclassLabel ?superclassDescription
        WHERE {
          SERVICE <http://localhost:3030/ds/query> {
            # Finding the local identifier for "Energy"
            ?superclassLocal rdfs:label "Energy"@en.
            reo:Renewable_Energy rdfs:subClassOf ?superclassLocal.
            OPTIONAL { ?superclassLocal rdfs:label ?superclassLabelLocal. }
            OPTIONAL { ?superclassLocal rdfs:comment ?superclassDescriptionLocal. }
          }

          SERVICE <https://query.wikidata.org/sparql> {
            # Use the Wikidata identifier for "renewable resource"
            wd:Q1138571 wdt:P279 ?superclass.
            ?superclass rdfs:label ?superclassLabel.
            OPTIONAL { ?superclass schema:description ?superclassDescription. }
            FILTER(LANG(?superclassLabel) = "en")
            FILTER(LANG(?superclassDescription) = "en")
          }
        }
    """

def generate_query2():
    return """
        # Second SPARQL Query
        PREFIX re: <http://www.w3.org/2000/10/swap/reason#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <http://schema.org/>
        PREFIX wikibase: <http://wikiba.se/ontology#>
        PREFIX bd: <http://www.bigdata.com/rdf#>
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>

        SELECT DISTINCT ?superclass ?superclassLabel ?superclassDescription
        WHERE {
          SERVICE <http://localhost:3030/ds/query> {
            # Finding the local identifier for "Energy"
            ?superclassLocal rdfs:label "Energy"@en.
            reo:Renewable_Energy rdfs:subClassOf ?superclassLocal.
            OPTIONAL { ?superclassLocal rdfs:label ?superclassLabelLocal. }
            OPTIONAL { ?superclassLocal rdfs:comment ?superclassDescriptionLocal. }
          }

          SERVICE <https://query.wikidata.org/sparql> {
            # Use the Wikidata identifier for "renewable resource"
            wd:Q12705 wdt:P279 ?superclass.
            ?superclass rdfs:label ?superclassLabel.
            OPTIONAL { ?superclass schema:description ?superclassDescription. }
            FILTER(LANG(?superclassLabel) = "en")
            FILTER(LANG(?superclassDescription) = "en")
          }
        }
    """


def generate_local_query2():
    return """
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        # Local SPARQL Query
        SELECT ?Renewable_Energy
        WHERE {
            ?Renewable_Energy rdf:type reo:Renewable_Energy.
        }
    """

def generate_query3():
    return """
        # Third SPARQL Query
            PREFIX re: <http://www.w3.org/2000/10/swap/reason#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX schema: <http://schema.org/>
            PREFIX wikibase: <http://wikiba.se/ontology#>
            PREFIX bd: <http://www.bigdata.com/rdf#>
            PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
            PREFIX wd: <http://www.wikidata.org/entity/>
            PREFIX wdt: <http://www.wikidata.org/prop/direct/>

            SELECT DISTINCT ?superclass ?superclassLabel ?superclassDescription
            WHERE {
              SERVICE <http://localhost:3030/ds/query> {
                # Finding the local identifier for "Energy"
                ?superclassLocal rdfs:label "Energy"@en.
                reo:Facilities rdfs:subClassOf ?superclassLocal.
                OPTIONAL { ?superclassLocal rdfs:label ?superclassLabelLocal. }
                OPTIONAL { ?superclassLocal rdfs:comment ?superclassDescriptionLocal. }
              }

              SERVICE <https://query.wikidata.org/sparql> {
                # Use the Wikidata identifier for "renewable resource"
                wd:Q56397239 wdt:P279 ?superclass.
                ?superclass rdfs:label ?superclassLabel.
                OPTIONAL { ?superclass schema:description ?superclassDescription. }
                FILTER(LANG(?superclassLabel) = "en")
                FILTER(LANG(?superclassDescription) = "en")
              }
            }

    """

def generate_query4():
    return """
        PREFIX re: <http://www.w3.org/2000/10/swap/reason#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <http://schema.org/>
        PREFIX wikibase: <http://wikiba.se/ontology#>
        PREFIX bd: <http://www.bigdata.com/rdf#>
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>

        SELECT DISTINCT ?superclass ?superclassLabel ?superclassDescription
        WHERE {
        SERVICE <http://localhost:3030/ds/query> {
            ?superclassLocal rdfs:label "Facilities"@en.
            reo:Producers rdfs:subClassOf ?superclassLocal.
        }

        SERVICE <https://query.wikidata.org/sparql> {
            wd:Q159719 wdt:P279 ?superclass.
            ?superclass rdfs:label ?superclassLabel.
            OPTIONAL { ?superclass schema:description ?superclassDescription. }
            FILTER(LANG(?superclassLabel) = "en")
        }
        }


    """
def generate_local_query4():
    return """
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        # Local SPARQL Query
        SELECT ?Producers
        WHERE {
            ?Producers rdf:type reo:Producers.
        }
    """

def generate_query5():
    return """
        PREFIX re: <http://www.w3.org/2000/10/swap/reason#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <http://schema.org/>
        PREFIX wikibase: <http://wikiba.se/ontology#>
        PREFIX bd: <http://www.bigdata.com/rdf#>
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>

        SELECT DISTINCT ?superclass ?superclassLabel ?superclassDescription
        WHERE {
        SERVICE <http://localhost:3030/ds/query> {
            ?superclassLocal rdfs:label "Facilities"@en.
            reo:Sensors rdfs:subClassOf ?superclassLocal.
        }

        SERVICE <https://query.wikidata.org/sparql> {
            wd:Q167676 wdt:P279 ?superclass.
            ?superclass rdfs:label ?superclassLabel.
            OPTIONAL { ?superclass schema:description ?superclassDescription. }
            FILTER(LANG(?superclassLabel) = "en")
    		FILTER(LANG(?superclassDescription) = "en")

        }
        }
    """
def generate_local_query5():
    return """
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?Sensors
            WHERE {
                ?Sensors rdf:type reo:Sensors.
            }
    """

def generate_query6():
    return """
        PREFIX re: <http://www.w3.org/2000/10/swap/reason#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <http://schema.org/>
        PREFIX wikibase: <http://wikiba.se/ontology#>
        PREFIX bd: <http://www.bigdata.com/rdf#>
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>

        SELECT DISTINCT ?superclass ?superclassLabel ?superclassDescription
        WHERE {
        SERVICE <http://localhost:3030/ds/query> {
            ?superclassLocal rdfs:label "Sensors"@en.
            reo:Notifications rdfs:subClassOf ?superclassLocal.
        }

        SERVICE <https://query.wikidata.org/sparql> {
            wd:Q2150504 wdt:P279 ?superclass.
            ?superclass rdfs:label ?superclassLabel.
            OPTIONAL { ?superclass schema:description ?superclassDescription. }
            FILTER(LANG(?superclassLabel) = "en")
    		FILTER(LANG(?superclassDescription) = "en")

        }
        }
    """

def generate_local_query6():
    return """
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?Notifications
            WHERE {
                ?Notifications rdf:type reo:Notifications.
            }
    """

def generate_query7():
    return """
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>

        SELECT ?renewableEnergy
        WHERE {
        ?renewableEnergy rdf:type reo:Renewable_Energy.
        ?renewableEnergy reo:produced_by ?producer.

        {
            SELECT ?renewableEnergy (COUNT(?producer) AS ?producerCount)
            WHERE {
            ?renewableEnergy rdf:type reo:Renewable_Energy.
            ?renewableEnergy reo:produced_by ?producer.
            }
            GROUP BY ?renewableEnergy
        }

        FILTER (?producerCount<=2)
        }
    """

def generate_query8():
    return """
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>

        SELECT ?producer
        WHERE {
        ?producer reo:checked_by ?sensor.
        ?sensor rdf:type reo:Sensors.
        }
        GROUP BY ?producer
        HAVING (COUNT(?sensor)<=4)
    """    

def generate_query9():
    return """
        PREFIX reo: <http://www.semanticweb.org/talhaalperasav/ontologies/2023/11/untitled-ontology-33#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>

        SELECT ?sensor
        WHERE {
        ?sensor reo:triggers ?notification.
        ?notification rdf:type reo:Notifications.
        }
        GROUP BY ?sensor
        HAVING (COUNT(?notification)<=4)
    """    

if __name__ == '__main__':
    app.run(debug = True)