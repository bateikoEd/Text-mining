from class_scrapping import Scrapping

object = Scrapping()

start_len = object.len_of_news()
object.nz_scrapping()
object.bbc_scraping()
end_len = object.len_of_news()
print(f"count of added news:\t{end_len - start_len}")
# object.to_all_txt()
