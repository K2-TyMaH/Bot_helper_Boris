from __future__ import annotations
from address_book import address_book
from boris import boris, dobriy_den, slava_ukraine

def main():
    """
   The user simply launches the bot and selects the desired function.
    """
    try:        
        dobriy_den()
        slava_ukraine()
        boris()
     
    except Exception:
        print("\nAn unexpected error has occurred...")
        boris()        

    finally:
        address_book.save_address_book()           


if __name__ == '__main__':
    main()
