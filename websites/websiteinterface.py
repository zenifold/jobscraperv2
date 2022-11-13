# Author: Olin Gallet
# Date: 5/11/2022
#
# The WebsiteInterface is to be implemented by all potential websites
# that would be crawled.  It provides an abstract function for scraping the website.

from abc import ABC, abstractmethod
from playwright.async_api import async_playwright, Browser
from .observers.observerinterface import ObserverInterface
from .jobdata import JobData

class WebsiteInterface(ABC):
    #15 second default timeout
    _DEFAULT_TIMEOUT = 30000

    def __init__(self):
        self._observers = []

    @abstractmethod
    async def scrape(self, browser:Browser):
        pass

    def subscribe (self, observer:ObserverInterface):
        ''' Subscribes the given observer for notifications for jobs found on this site.
        :param: observer the observer to notify
        :type: ObserverInterface
        '''
        self._observers.append(observer)

    async def notify (self, job_data:JobData):
        ''' Notify all observers with provided job data
        :param: job_data the job data
        :type: JobData
        '''
        for observer in self._observers:
            await observer.notify(job_data)