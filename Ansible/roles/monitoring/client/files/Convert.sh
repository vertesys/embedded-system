#!/bin/sh

## HEADER ##############################################################################################
cat <<EOLINE > /home/pi/.fantastics/monitoring/index.html
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="icon" href="favicon.ico">
        <title>Raspberry Monitoring</title>
        <link href="bootstrap.min.css" rel="stylesheet">
        <script src="jquery.min.js"></script>
    </head>
    <body>
        <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
            <a class="navbar-brand" href="#">FANTASTICS</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" 
            data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" 
            aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <ul class="navbar-nav mr-auto">
                </ul>
            </div>
        </nav>
        <main role="main" class="container-fluid">
EOLINE
## CONTENT #############################################################################################
        file=$(cat /home/pi/.fantastics/monitoring/temporary.html)
        file=$(echo $file | sed 's/\[1m\[100;97/<\/table><table><th>/g') 
        file=$(echo $file | sed 's/\[0m/<\/th>/g') 
        file=$(echo $file | sed 's/\[32;40m/<\/td><\/tr><tr><td>/g') 
        file=$(echo $file | sed 's/\[37;40m/<\/td><td>/g') 

        file=$(echo $file | sed 's/\[31;40mOFFLINE/<\/td><td>OFFLINE<\/td>/g') 
        file=$(echo $file | sed 's/\[31;40mINACTIVE/<\/td><td>INACTIVE<\/td>/g') 

        file=$(echo $file | sed 's/<table>/<table class="table table-sm table-bordered">/g')
        file=$(echo $file | sed 's/<\/table>/<\/td><\/tr><\/table>/g')

        file=$(echo $file | sed 's/<th>/<th class="bg-dark text-white">/g')

        file=$(echo $file | tr -s ' ')
        echo $file >> /home/pi/.fantastics/monitoring/index.html
        echo "</table>" >> /home/pi/.fantastics/monitoring/index.html
        sed -i 's/\x1b//g' /home/pi/.fantastics/monitoring/index.html
## FOOTER ##############################################################################################
cat <<EOL >> /home/pi/.fantastics/monitoring/index.html
            <div class="row">
                <div class="col-sm-6 col-lg-6 tableau-1">
                </div>
                <div class="col-sm-6 col-lg-6 tableau-2">
                </div>
            </div>
            <div class="row">
                <div class="col-sm-6 col-lg-6 tableau-3">
                </div>
                <div class="col-sm-6 col-lg-6 tableau-4">
                </div>
            </div>
            <div class="row">
                <div class="col-sm-6 col-lg-6 tableau-5">
                </div>
                <div class="col-sm-6 col-lg-6 tableau-6">
                </div>
            </div>
            <div class="row">
                <div class="col-sm-6 col-lg-6 tableau-7">
                </div>
                <div class="col-sm-6 col-lg-6 tableau-8">
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12 col-lg-12 tableau-9">
                </div>
            </div>
        </main>
        <script>
        \$(document).ready(function() {
            var nombre = 1
            \$("table").each(function(){
                var table = \$(this);
                var title = \$(this).find("th").text();
                title = title.substring(2, title.length);
                var header = \$(this).find("th").attr('colspan',2).text(title);
                if (\$(".tableau-" + nombre).length) {
                    \$(this).appendTo(\$(".tableau-" + nombre))
                }
                nombre = nombre + 1
            });
        });
        </script>
    </body>
</html>
EOL

#######################################################################################################
