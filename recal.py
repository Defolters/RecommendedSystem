import random

#you should download Ratings!!!

def find_user_movie_rat(user_id, movie_id):
    result = None
    for i in range(Ratings.shape[0]):
        if user_id == Ratings.userId[i] and movie_id == Ratings.movieId[i]:
            result = Ratings.rating[i]
            break
    return result

def calculate_recal(n_users, n_movies, function):
    users_list = []
    
    for i in range(n_users):
        users_list.append(random.choice (Ratings.userId))
        
    mean_recal = []
    for i in users_list:
        predicted_ids = function(i, n_movies)
        recal = 0
        for x in predicted_ids:
            tmp_res = find_user_movie_rat(i, x)
            if tmp_res is None:
                continue
            if tmp_res >= 3.6:
                recal+=1
            print(f'user_id = {i}, movie_id= {x}, rating in table= {tmp_res}')
        mean_recal.append(recal/n_movies)
    
    return np.mean(mean_recal)       