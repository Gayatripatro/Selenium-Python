### Types of webdriver commands
1) Application Commands
2) conditional Commands
3) Browser Commands
4) Navigational Commands
5) Wait Commands

**1) Application Commands**
* title - to capture the title of the current webpage
* get() - opening the apprication url
* current_url - to capture the current url of the webpage
* page_source - to capture the source code of the webpage
  
**2) Conditional Commands**
* is_displayed() - if the locator is displayed it will return TRUE else it will reture FALSE
* is_enabled() - if the locator is enabled it will return TRUE else it will reture FALSE
* is_selected() - if the Radio button/ checkBox is selected it will return TRUE else it will reture FALSE

**3) Browser Commands**
* close() - close the signle browser window(where driver focused/ here process will not closed it will run in background)
* quite() - close the multiple browser windows (this will kill the process)

**4) Navigational Commands**
* back() - if u open 2 uls using selenium then it will go back to previous url
* foward() - it will forward to next url
* refresh() - it will refresh the existing webpage

**5) Wait Commands**
* For fixing Synchronization problem we are using wait commands. (**Synchronization Problem** means sometime for loading the whole page it will take time so we need to intetionally hold our selenium scripts for sometime)
* Implicit wait -

              - It will apply for whole locators of the webpage
              - Ex: driver.implicitly_wait(10)  -> if the element is available within 10 sec it proceed to execute further statements
              - if the element is not available within the time then it will through exception
     
* Explicit wait -

              - EX: from selenium.webdriver.support.wait import WebDriverWait
                    from selenium.webdriver.support import expected_conditions as EC
                    driver = webdriver.Chrome()
                    mywait = WebDriverWait(driver,10) # explicit wait declaration
              or    mywait = WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,ElementNotVisibleExeception,ElementNotSelectableException]) # it will handel the exeception also so that if the elemet not available then it will not through the exception and other lines will execute
              or    mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleExeception,ElementNotSelectableException]) # it will go and check every 2 sec that the element is available or not if available it will perorm the task
                    driver.get("app url")
                    webelement Naame = mywait.until(EC.presence_of_element_lcated(By.XPATH,"//xpath")) # it will wait untill the location is not displayed. Once the element is available it will return the element
                    webelement Naame.click()


### Difference between FindElement() and FindElements()
* find_element() -
  
                  - Returns a signle webelement
                  - If we pass xpath of multiple elements by using find_element() it will select 1st elements only
                  - If we provide xpath with contains multiple elements and by using text we are trying to perform any task it will through NoSuchElement Exception

* find_elements() -


                  - Returns a list of webelements
                  - If we provide xpath of multiple elements by using find_elements() it will give all the value one by one
                  - If we provide xpath with contains multiple elements and by using text we are trying to perform any task it will perform the particular task


  ### Diference between text and get_attribute()
* text -

          - always returns the inner text of the element
          - Ex: <input id = '123 name='gayu'> EmailId: </input> ---> EmailId: is the inner text for this element
          - Mostly links were having inner text
          - If we dont have inner text for a locator and we are trying to get the text that time it will not return any value
 

* get_attribute() - 

           - It will return any value of the web elements
           - If we dont have inner text for a locator and we need to get the text for that particular web element that time we can use get_attribute()
           - Synstx : element_name.get_attribute('value')  --> in value u can provide name/class name/id/value(innertext)
