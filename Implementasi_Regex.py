import re
from typing import List, Dict, Optional

class RegexValidator:
    """
    Class untuk validasi berbagai format data menggunakan Regular Expression
    """
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validasi format email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_phone_id(phone: str) -> bool:
        """Validasi nomor telepon Indonesia (format: +62/0/62)"""
        pattern = r'^(\+62|62|0)[0-9]{9,12}$'
        return bool(re.match(pattern, phone))
    
    @staticmethod
    def validate_url(url: str) -> bool:
        """Validasi format URL"""
        pattern = r'^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)$'
        return bool(re.match(pattern, url))
    
    @staticmethod
    def validate_nik(nik: str) -> bool:
        """Validasi NIK Indonesia (16 digit)"""
        pattern = r'^\d{16}$'
        return bool(re.match(pattern, nik))
    
    @staticmethod
    def validate_password(password: str) -> Dict[str, bool]:
        """
        Validasi kekuatan password
        Return: dict dengan kriteria yang terpenuhi
        """
        return {
            'min_length': len(password) >= 8,
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_digit': bool(re.search(r'\d', password)),
            'has_special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        }


class RegexExtractor:
    """
    Class untuk ekstraksi data dari teks menggunakan Regular Expression
    """
    
    @staticmethod
    def extract_emails(text: str) -> List[str]:
        """Ekstrak semua email dari teks"""
        pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_phone_numbers(text: str) -> List[str]:
        """Ekstrak nomor telepon Indonesia dari teks"""
        pattern = r'(\+62|62|0)[0-9]{9,12}'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_urls(text: str) -> List[str]:
        """Ekstrak semua URL dari teks"""
        pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_hashtags(text: str) -> List[str]:
        """Ekstrak hashtag dari teks"""
        pattern = r'#\w+'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_mentions(text: str) -> List[str]:
        """Ekstrak mention (@username) dari teks"""
        pattern = r'@\w+'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_dates(text: str) -> List[str]:
        """Ekstrak tanggal format DD-MM-YYYY atau DD/MM/YYYY"""
        pattern = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b'
        return re.findall(pattern, text)


class RegexReplacer:
    """
    Class untuk manipulasi teks menggunakan Regular Expression
    """
    
    @staticmethod
    def mask_email(text: str) -> str:
        """Sembunyikan email dengan masking"""
        pattern = r'\b([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b'
        return re.sub(pattern, r'\1***@\2', text)
    
    @staticmethod
    def mask_phone(text: str) -> str:
        """Sembunyikan nomor telepon (tampilkan 4 digit terakhir saja)"""
        pattern = r'(\+62|62|0)(\d{5,8})(\d{4})'
        return re.sub(pattern, r'\1****\3', text)
    
    @staticmethod
    def remove_html_tags(text: str) -> str:
        """Hapus semua HTML tags dari teks"""
        pattern = r'<[^>]+>'
        return re.sub(pattern, '', text)
    
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """Normalisasi whitespace (hapus multiple spaces)"""
        pattern = r'\s+'
        return re.sub(pattern, ' ', text).strip()
    
    @staticmethod
    def censor_profanity(text: str, words: List[str]) -> str:
        """Sensor kata-kata tertentu"""
        for word in words:
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            text = pattern.sub('*' * len(word), text)
        return text


# ===== CONTOH PENGGUNAAN =====
def demo():
    print("=" * 60)
    print("DEMO IMPLEMENTASI REGEX DI PYTHON")
    print("=" * 60)
    
    # 1. VALIDASI
    print("\n1. VALIDASI DATA")
    print("-" * 60)
    
    validator = RegexValidator()
    
    # Test Email
    test_emails = ["user@example.com", "invalid.email", "test@domain.co.id"]
    print("\nValidasi Email:")
    for email in test_emails:
        result = validator.validate_email(email)
        print(f"  {email:<30} -> {'[Valid]' if result else '[Invalid]'}")
    
    # Test Phone
    test_phones = ["081234567890", "+6281234567890", "021123456"]
    print("\nValidasi Nomor Telepon:")
    for phone in test_phones:
        result = validator.validate_phone_id(phone)
        print(f"  {phone:<30} -> {'[Valid]' if result else '[Invalid]'}")
    
    # Test Password
    test_password = "MyP@ssw0rd123"
    print(f"\nValidasi Password: {test_password}")
    pwd_result = validator.validate_password(test_password)
    for criteria, status in pwd_result.items():
        print(f"  {criteria:<20} -> {'[OK]' if status else '[NO]'}")
    
    # 2. EKSTRAKSI
    print("\n\n2. EKSTRAKSI DATA")
    print("-" * 60)
    
    extractor = RegexExtractor()
    
    sample_text = """
    Hubungi kami di email: info@company.com atau support@company.co.id
    Telepon: 081234567890 atau +6287654321098
    Website: https://www.example.com dan http://blog.example.com
    Follow us #Python #Regex @username @company
    Event tanggal: 15-08-2024 dan 20/12/2024
    """
    
    print("\nTeks Sample:")
    print(sample_text)
    
    print("\nHasil Ekstraksi:")
    print(f"  Emails     : {extractor.extract_emails(sample_text)}")
    print(f"  Phones     : {extractor.extract_phone_numbers(sample_text)}")
    print(f"  URLs       : {extractor.extract_urls(sample_text)}")
    print(f"  Hashtags   : {extractor.extract_hashtags(sample_text)}")
    print(f"  Mentions   : {extractor.extract_mentions(sample_text)}")
    print(f"  Dates      : {extractor.extract_dates(sample_text)}")
    
    # 3. MANIPULASI
    print("\n\n3. MANIPULASI TEKS")
    print("-" * 60)
    
    replacer = RegexReplacer()
    
    sensitive_text = "Email saya user@gmail.com dan HP 081234567890"
    print(f"\nTeks Original : {sensitive_text}")
    print(f"Mask Email    : {replacer.mask_email(sensitive_text)}")
    print(f"Mask Phone    : {replacer.mask_phone(sensitive_text)}")
    
    html_text = "<p>Ini adalah <b>teks HTML</b> dengan <a href='#'>link</a></p>"
    print(f"\nHTML Original : {html_text}")
    print(f"Remove HTML   : {replacer.remove_html_tags(html_text)}")
    
    messy_text = "Ini    teks   dengan    banyak      spasi"
    print(f"\nMessy Text    : {messy_text}")
    print(f"Normalized    : {replacer.normalize_whitespace(messy_text)}")
    
    profane_text = "Ini teks dengan kata badword dan badword lainnya"
    print(f"\nProfane Text  : {profane_text}")
    print(f"Censored      : {replacer.censor_profanity(profane_text, ['badword'])}")


if __name__ == "__main__":
    demo()