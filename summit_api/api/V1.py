import frappe
from summit_api.utils import success_response, error_response
import summit_api.api.v1.banner as banner
import summit_api.api.v1.brand as brand
import summit_api.api.v1.otp as otp
import summit_api.api.v1.cart as cart
import summit_api.api.v1.catalog as catalog
import summit_api.api.v1.coupon_code as coupon_code
import summit_api.api.v1.customer_address as customer_address
import summit_api.api.v1.filter as filter
import summit_api.api.v1.mega_menu as mega_menu
import summit_api.api.v1.order as order
import summit_api.api.v1.product as product
import summit_api.api.v1.registration as registration
import summit_api.api.v1.seller as seller
import summit_api.api.v1.signin as signin
import summit_api.api.v1.profile as profile
import summit_api.api.v1.dealer as dealer
import summit_api.api.v1.store_credit as store_credit
import summit_api.api.v1.gl as gl
import summit_api.api.v1.wishlist as wishlist
import summit_api.api.v1.seo as seo
import summit_api.api.v1.utils as utils


class V1():
    def __init__(self):
        self.methods = {
            'banner': ['get'],
            'otp': ['send_otp', 'verify_otp'],
            "brand": ['get', 'get_product_list', 'get_product_details'],
            "cart": ['get_list', 'put_products', 'delete_products', 'clear_cart','request_for_quotation','get_quotation_history'],
            "catalog": ['get', 'get_items'],
            "coupon_code": ['put', 'delete'],
            "customer_address": ['get', 'put'],
            "dealer": ['get_dealer'],
            "profile": ['get_profile','customer_inquiry', 'ageing_report', 'get_transporters'],
            "filter": ['get_filters'],
            "mega_menu": ['get', 'breadcrums'],
            "order": ['get_list', 'get_summary', 'get_order_id', 'place_order', 'return_replace_item', 'get_razorpay_payment_url', 'get_order_details', 'recently_bought'],
            "product": ['get_list', 'get_details', 'get_cyu_categories', 'get_variants', 'get_recommendation', 'get_top_categories', "get_tagged_products", "check_availability", "get_categories"],
            "registration": ['add_subscriber','customer_signup', 'change_password', 'reset_password', 'send_reset_link', 'create_registration'],
            "seller": ['get'],
            "signin": ['signin', 'get_user_profile', 'signin_as_guest', 'get_redirecting_urls', 'login_via_token'],
            "store_credit": ['put', 'delete'],
            "gl": ['get_dealer_ledger', 'get_ledger_summary', "export_ledger"],
            "wishlist": ["add_to_wishlist", "remove_from_wishlist", "get_wishlist_items"],
            "seo": ["get_meta_tags","get_site_map"],
            "utils": ["validate_pincode", "get_cities", 'get_states', 'get_countries']
        }

    def class_map(self, kwargs):
        entity = kwargs.get('entity')
        method = kwargs.get('method')
        if self.methods.get(entity):
            if method in self.methods.get(entity):
                function = f"{kwargs.get('entity')}.{kwargs.get('method')}({kwargs})"
                return eval(function)
            else:
                return error_response("Method Not Found!")
        else:
            return error_response("Entity Not Found!")
