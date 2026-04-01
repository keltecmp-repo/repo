# -*- coding: utf-8 -*-
"""
DOH.PY - DNS over HTTPS
Usado pelo F4MTESTER para resolver DNS
"""

import socket
import requests

_original_getaddrinfo = socket.getaddrinfo
_dns_cache = {}

def DNSOverrideDoH():
    """Ativa DNS over HTTPS usando Cloudflare"""
    
    def custom_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
        # Se já está em cache, usa
        if host in _dns_cache:
            return _dns_cache[host]
        
        # Tenta resolver via DoH (Cloudflare)
        try:
            doh_url = f"https://cloudflare-dns.com/dns-query?name={host}&type=A"
            headers = {"accept": "application/dns-json"}
            
            response = requests.get(doh_url, headers=headers, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                
                if "Answer" in data and len(data["Answer"]) > 0:
                    ip = data["Answer"][0]["data"]
                    
                    # Formato que socket.getaddrinfo retorna
                    result = [
                        (socket.AF_INET, socket.SOCK_STREAM, 6, '', (ip, port))
                    ]
                    
                    # Salva em cache
                    _dns_cache[host] = result
                    
                    return result
        
        except:
            pass
        
        # Se falhar, usa DNS padrão
        result = _original_getaddrinfo(host, port, family, type, proto, flags)
        _dns_cache[host] = result
        return result
    
    # Substitui função global
    socket.getaddrinfo = custom_getaddrinfo