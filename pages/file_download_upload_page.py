from playwright.sync_api import Page

class FileTransferPage:
    """
    This Class is for File Upload and Download Handling operations
    """
    def __init__(self, page:Page):
        self.page = page