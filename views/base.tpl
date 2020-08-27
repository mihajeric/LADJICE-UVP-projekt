<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <style>

        .igra {
            margin:auto;
            margin-top: 1em;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content:space-evenly;
        }
        .mreza {
            width: 45vw;
            height: 45vw;
            max-width: 50vh;
            max-height: 50vh;
            display: block;
            background-color: #aaa;
            display:inline-block;
            font-size: 0;
        }

        .polje {
            width: 10%;
            height: 10%;
            background-color: #aaa;
            display:inline-block;
            border: 1px solid #333;
            margin: 0px;
        }

        .polje-neznano {
            background-color: #aaa;
        }
        .polje-ladjica {
            background-color: rgb(255, 174, 0);
        }
        .polje-ladjica-potopljena {
            background-color: rgb(163, 0, 0);
        }
        .polje-prazno {
            background-color: rgb(102, 102, 255);
        }

        .vsebina {
            max-width: 110vh;
            margin: auto;
        }
    </style>
    <title>Ladjice</title>
</head>
<body>
    <div class="text-center vsebina">
        {{!base}}
    </div>
</body>
</html>