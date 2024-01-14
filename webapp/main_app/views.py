from django.shortcuts import render, redirect
from .forms import WordPairForm, WordPair
from .helpers.clases import Question_card, Library_card
from .helpers.functions import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from wordnote.db.db import Create_cursor
from pathlib import Path
import json

open = 0
home_dir = Path.home()
db_path = home_dir / 'my_database.db'

def home(request):
    db_helper = Create_cursor(db_path)
    db_helper.create_connection()
    data = db_helper.data_list()

    global open
    if open == 0:
        open = 1
        print("First Opening")
        data = db_helper.data_list()
        word_pairs_all = []
        for lib_obj in range(len(data[0])):
            lib_obj = Library_card(data[1][lib_obj], data[2][lib_obj], data[3][lib_obj], data[4][lib_obj],
                                   data[0][lib_obj])
            word_pairs_all.append(lib_obj)

        for word_pair in word_pairs_all:
            if word_pair.progress >= 100:
                current_time = now_time()
                different_time = current_time - word_pair.time
                if different_time >= 750:
                    db_helper.edit_progress_record(90,word_pair.base_id)


    db_helper.close_database()
    return render (request, 'main_app/home.html', {'word_pairs': data})

def test(request):
    db_helper = Create_cursor(db_path)
    db_helper.create_connection()
    data = db_helper.data_list()
    word_pairs_all = []
    for lib_obj in range(len(data[0])):
        lib_obj = Library_card(data[1][lib_obj], data[2][lib_obj], data[3][lib_obj], data[4][lib_obj], data[0][lib_obj])
        word_pairs_all.append(lib_obj)

    db_helper.close_database()

    word_pairs_valid_all = ()
    cards = []
    test_lenght = 20
    random_wrong_answers = ()

    # Making word_pairs_valid_all tuple with valid objects(which contains words and translations)
    for word_pairs_valid in word_pairs_all:
        if word_pairs_valid.progress < 100:
            word_pairs_valid_all = word_pairs_valid_all +(word_pairs_valid, )

    # Condition under which test will not go if counts of words is not enough
    if len(word_pairs_valid_all) == 0 or len(word_pairs_all) < 4:
        return render (request, 'main_app/home.html')
    # If valid words less than standard lenght test test_lenght become equal to count of valid words
    if len(word_pairs_valid_all) < test_lenght:
        test_lenght = len(word_pairs_valid_all)

    # start function to making tuple of random numbers
    random_tuple = generate_random(0, len(word_pairs_valid_all), test_lenght)

    #  making tuple with different answers
    for wrong_answer in random_tuple:
        while True:
            random_answers = generate_random(0, len(word_pairs_all), 3)
            random_answers_id = [word_pairs_all[random_answers[0]].base_id,
                                 word_pairs_all[random_answers[1]].base_id,
                                 word_pairs_all[random_answers[2]].base_id,
                                 ]
            if word_pairs_valid_all[wrong_answer].base_id in random_answers_id:
                continue
            else:
                random_wrong_answers = random_wrong_answers + (random_answers,)
                break


    for elem in range(0, test_lenght):
        card = Question_card(word_pairs_valid_all[random_tuple[elem]].word,
                                word_pairs_valid_all[random_tuple[elem]].translate,
                                word_pairs_all[random_wrong_answers[elem][0]].translate,
                                word_pairs_all[random_wrong_answers[elem][1]].translate,
                                word_pairs_all[random_wrong_answers[elem][2]].translate,
                                word_pairs_valid_all[random_tuple[elem]].base_id
                             )
        cards.append(card)


    json_data = json.dumps([obj.__dict__ for obj in cards])
    context = {'json_data': json_data}

    return render(request, 'main_app/test.html', context)

def test_reverse(request):
    db_helper = Create_cursor(db_path)
    db_helper.create_connection()
    data = db_helper.data_list()
    word_pairs_all = []
    for lib_obj in range(len(data[0])):
        lib_obj = Library_card(data[1][lib_obj], data[2][lib_obj], data[3][lib_obj], data[4][lib_obj], data[0][lib_obj])
        word_pairs_all.append(lib_obj)

    db_helper.close_database()

    word_pairs_valid_all = ()
    cards = []
    test_lenght = 20
    random_wrong_answers = ()

    # Making word_pairs_valid_all tuple with valid objects(which contains words and translations)
    for word_pairs_valid in word_pairs_all:
        if word_pairs_valid.progress < 100:
            word_pairs_valid_all = word_pairs_valid_all +(word_pairs_valid, )

    # Condition under which test will not go if counts of words is not enough
    if len(word_pairs_valid_all) == 0 or len(word_pairs_all) < 4:
        return render (request, 'main_app/home.html')
    # If valid words less than standard lenght test test_lenght become equal to count of valid words
    if len(word_pairs_valid_all) < test_lenght:
        test_lenght = len(word_pairs_valid_all)

    # start function to making tuple of random numbers
    random_tuple = generate_random(0, len(word_pairs_valid_all), test_lenght)

    #  making tuple with different answers
    for wrong_answer in random_tuple:
        while True:
            random_answers = generate_random(0, len(word_pairs_all), 3)
            random_answers_id = [word_pairs_all[random_answers[0]].base_id,
                                 word_pairs_all[random_answers[1]].base_id,
                                 word_pairs_all[random_answers[2]].base_id,
                                 ]
            if word_pairs_valid_all[wrong_answer].base_id in random_answers_id:
                continue
            else:
                random_wrong_answers = random_wrong_answers + (random_answers,)
                break


    for elem in range(0, test_lenght):
        card = Question_card(word_pairs_valid_all[random_tuple[elem]].translate,
                                word_pairs_valid_all[random_tuple[elem]].word,
                                word_pairs_all[random_wrong_answers[elem][0]].word,
                                word_pairs_all[random_wrong_answers[elem][1]].word,
                                word_pairs_all[random_wrong_answers[elem][2]].word,
                                word_pairs_valid_all[random_tuple[elem]].base_id
                             )
        cards.append(card)


    json_data = json.dumps([obj.__dict__ for obj in cards])
    context = {'json_data': json_data}

    return render(request, 'main_app/test.html', context)

# views.py

def add_words(request):
    db_helper = Create_cursor(db_path)
    db_helper.create_connection()

    if request.method == 'POST':
        form = WordPairForm(request.POST)
        if form.is_valid():
            form.save()
            word_pairs_all = WordPair.objects.all()
            for word_pair in word_pairs_all:
                new_w = word_pair.word
                tran_w = word_pair.translation
                prog = 5
                time = now_time()
                word = {'New_word': new_w, 'Translation': tran_w, 'Progress': prog, 'Time': time}
                db_helper.write_new_word(word)

                word_pairs_all.delete()

            db_helper.close_database()
            return redirect('add_words')  # Redirect to the same page after saving
    else:
        form = WordPairForm()

    return render(request, 'main_app/add_words.html', {'form': form})
def library(request):
    db_helper = Create_cursor(db_path)
    db_helper.create_connection()
    data = db_helper.data_list()
    word_pairs = []
    for lib_obj in range(len(data[0])):
        lib_obj = Library_card(data[1][lib_obj],data[2][lib_obj],data[3][lib_obj],data[4][lib_obj],data[0][lib_obj])
        word_pairs.append(lib_obj)

    print(f'Length is {len(word_pairs)}')
    db_helper.close_database()
    return render(request, 'main_app/library.html', {'word_pairs': word_pairs})

  # To disable CSRF protection for this view (for demonstration purposes)
@csrf_exempt
def save_changes(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        word_pair_id = data.get('wordPairId')
        new_word = data.get('newWord')
        new_translation = data.get('newTranslation')
        new_progress = data.get('progressValue')
        time = now_time()

        db_helper = Create_cursor(db_path)
        db_helper.create_connection()
        db_helper.edit_word_record(new_word,word_pair_id)
        db_helper.edit_translation_record(new_translation, word_pair_id)
        db_helper.edit_progress_record(new_progress, word_pair_id)
        db_helper.edit_time_record(time, word_pair_id)
        db_helper.close_database()

        print('Changes saved successfully.')
        return JsonResponse({'success': True})


    print('Invalid request method.')
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def delete_word_pair(request):
    data = json.loads(request.body.decode('utf-8'))
    word_pair_id = data.get('wordPairId')

    db_helper = Create_cursor(db_path)
    db_helper.create_connection()
    db_helper.delete_record(word_pair_id)
    db_helper.close_database()
    return JsonResponse({'success': True})

@csrf_exempt
def change_progress(request):
    if request.method == 'POST':
        # Extract data from the POST request
        try:
            data = json.loads(request.body.decode('utf-8'))
            correctList = data.get('list1', [])
            wrongList = data.get('list2', [])
            db_helper = Create_cursor(db_path)
            db_helper.create_connection()
            table_row = 'Progress'

            for elem in correctList:
                progress = db_helper.get_record_by_id(table_row, elem)

                if progress > 95:
                    db_helper.edit_progress_record(100, elem)
                else:
                    progress += 5
                    db_helper.edit_progress_record(progress, elem)

            for elem in wrongList:
                progress = db_helper.get_record_by_id(table_row, elem)

                if progress < 5:
                    db_helper.edit_progress_record(0, elem)
                else:
                    progress -= 2.5
                    db_helper.edit_progress_record(progress, elem)

            db_helper.close_database()
            # Return a JSON response (optional)
            return JsonResponse({'success': True})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': str(e)}, status=400)
def options(request):

    return render (request, 'main_app/options.html',)


def trying(request):

    return render (request, 'main_app/trying.html',)