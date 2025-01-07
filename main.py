import os
import sys
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import logging
import stat
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
USERNAME = os.getenv("MoodleUs", "USER")
PASSWORD = os.getenv("MoodlePa", "PASS")
SHADOW = os.getenv("MoodleSh", "False").lower() == "true"
STATUT = os.getenv("MoodleSt")
COURSE_URL = os.getenv("MoodleCourseUrl")
ATTENDANCE_URL = os.getenv("MoodleAttendanceUrl")
path = os.path.dirname(__file__)

# Logging configuration
logging.basicConfig(
    filename='emergement.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

def ensure_executable(filepath):
    if not os.access(filepath, os.X_OK):
        logging.info(f"Rendant {filepath} exécutable.")
        os.chmod(filepath, os.stat(filepath).st_mode | stat.S_IEXEC)

def emergement():
    logging.info("Ouverture du navigateur Selenium.")

    options = Options()
    if SHADOW:
        options.add_argument('-headless')

    if ":\\" in os.getcwd():
        service = Service(executable_path=f".{path}/geckodriver")
    elif "darwin" in os.uname().sysname.lower():  # macOS check
        mac_driver = f"{path}/geckodriver_MAC"
        ensure_executable(mac_driver)
        service = Service(executable_path=mac_driver)
    else:
        service = Service(executable_path=f"{path}/geckodriver")

    driver = webdriver.Firefox(options=options, service=service)

    try:
        driver.get("https://moodle.univ-ubs.fr/")
        time.sleep(0.5)

        select_element = driver.find_element(By.ID, "idp")
        dropdown = Select(select_element)
        dropdown.select_by_visible_text("Université Bretagne Sud - UBS")

        select_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")
        select_button.click()
        time.sleep(1)

        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys(USERNAME)

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(PASSWORD)

        login_button = driver.find_element(By.XPATH, "//span[text()='SE CONNECTER']/parent::button")
        login_button.click()

        try:
            error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Mauvais identifiant / mot de passe')]")
            logging.warning("Mauvais Identifiant ou Mot de passe")
            if USERNAME == 'USER':
                logging.warning("Créez le fichier .env pour y stocker vos identifiants")
            driver.quit()
            return
        except NoSuchElementException:
            logging.info("Connexion réussie")

        time.sleep(1)

        driver.get(COURSE_URL)
        time.sleep(0.5)

        driver.get(ATTENDANCE_URL)
        time.sleep(0.5)

        try:
            link_element = driver.find_element(By.XPATH, "//a[contains(text(), 'Envoyer le statut de présence')]")
            link_href = link_element.get_attribute("href")
            driver.get(link_href)

            time.sleep(1)

            present_radio_button = driver.find_element(By.XPATH, f"//input[@type='radio' and @name='status'][following-sibling::span[text()='{STATUT}']]")
            present_radio_button.click()

            save_button = driver.find_element(By.XPATH, "//input[@type='submit' and @id='id_submitbutton']")
            save_button.click()

            logging.info("Statut envoyé avec succès")
            print("✅ Émargement effectué avec succès.")

        except NoSuchElementException:
            logging.warning("Impossible d'envoyer le statut, aucun bouton disponible")
            print("❌ Aucun bouton d'émargement disponible.")

    except Exception as e:
        logging.error(f"Une erreur est survenue: {e}")
        print(f"⚠️ Une erreur est survenue: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":

    # Run the emergement process
    emergement()
