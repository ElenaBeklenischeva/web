%import db_methods
<div class="counter" id='counts'>
<!--    <p class="text_counter">Всего посещений: {{all}}</p>
    <p class="text_counter">Сегодня: {{today}}</p>
    <p class="text_counter">Ваше последнее посещение: <br>{{last_visit}}</p>
    <p class="text_counter" id="resolution"></p>
    <p class="text_counter">Информация о браузере: {{browser}}</p>
    -->
    %string = db_methods.generate_img(text)
    <img src={{string}}>
    <p class="text_counter" id="resolution"></p>
    <p class="text_counter">Информация о браузере: {{browser}}</p>
</div>
