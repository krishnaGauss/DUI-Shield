#Selenium WebDriver options
HEADLESS_MODE=True  # Set to False to see browser
SELENIUM_TIMEOUT=30  # seconds to wait for elements to load

#Logger configs
LOG_LEVEL='INFO'  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE='dui.log'  # Log file name

#common phrases for confirm shaming
CONFIRM_SHAMING_PHRASES = [
    "Are you really sure?",
    "This action is irreversible.",
    "Think about the consequences.",
    "Do you really want to do this?",
    "Consider the impact of your choice.",
    "no thanks, i prefer to miss out",
    "i don't want to save money",
    "no, i like paying full price",
    "i'll pass on the savings",
    "no, i'm happy with my slow internet",
    "i'd rather not get updates",
    "skip the discount",    
    "I don't want premium features",
    "I prefer to miss out on updates",
    "I prefer staying in my current job"  
]

# Example: Keywords for disguised ads (in classes, IDs, or text)
DISGUISED_AD_KEYWORDS = [
    "ad", "advert", "sponsored", "promo", "recommended for you",
    "you might also like", "from our partners", "latest offers"
]

# Example: Keywords for sneak into basket
SNEAK_INTO_BASKET_KEYWORDS = [
    "add to order", "include extra", "premium support", "insurance", "warranty"
]