% import model
% rebase('base.tpl')

<form action="./polje" method="post">

    <h1 class="title">Ladjice</h1>

    <p>
    % if faza == model.POSTAVLJANJE:
        Izberi dolžino in orientacijo ladjice, potem pa jo s klikom na polje postavi
    % elif faza == model.STRELJANJE:
        Klikni na polje, kamor želiš streljati (na desni mreži)
    %elif faza == model.KONEC:
        Konec igre!
    % end
    <p>


    % if faza == model.POSTAVLJANJE:
        <div class="container">
            <div class="form-group">
                <label for="dolzina">Dolžina ladjice</label>
                <select class="form-control" id="dolzina" name="dolzina">
                    % for (dolzina, stevilo) in enumerate(dolzine_ladjic):
                        % if stevilo != 0:
                            <option {{"selected" if izbrana_dolzina==dolzina else ""}}>{{dolzina}}</option>
                        % end
                    % end
                </select>
            </div>
            <div class="form-group">
                <label for="orinetacija">Orientacija ladjice</label>
                <select class="form-control" id="orinetacija" name="orinetacija">
                    <option value="v" {{"selected" if izbrana_usmerjenost=="v" else ""}}>Vertikalna</option>
                    <option value="h" {{"selected" if izbrana_usmerjenost=="h" else ""}}>Horizontalna</option>
                </select>
            </div>
        </div>

        % if rezultat_poteze == model.ERROR:
            <h3>Neveljavna postavitev!</h3>
        % end

    % elif faza == model.KONEC:
        % if rezultat_poteze == model.ZMAGA:
            <h3>Zmagal si!</h3>
        % else:
            <h3>Izgubil si.</h3>
        % end
        <a href="./" class="btn btn-primary">Nazaj na začetek</a>

    % end


    <!--      Izris igralnih polj     -->

    <div class="igra">
        <div class="mreza">
            % for (indeks, polje) in enumerate(mreza_igralec_odkrita if faza == model.POSTAVLJANJE else mreza_igralec):
                % if faza == model.POSTAVLJANJE:
                    <input type="submit" name="polje" value="{{indeks}}" class="polje {{tipi_polj[polje]}}">
                % else:
                    <span class="polje {{tipi_polj[polje]}}"></span>
                % end
            % end
        </div>

        % if faza != model.POSTAVLJANJE:
            <div class="mreza">
                % for (indeks, polje) in enumerate(mreza_racunalnik):
                    <input type="submit" name="polje" value="{{indeks}}" class="polje {{tipi_polj[polje]}}">
                % end
            </div>
        % end
    </div>
</form>