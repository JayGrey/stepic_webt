# remove old settings
rm /etc/nginx/sites-enabled/test.conf
rm /etc/nginx/sites-enabled/default
rm /home/box/web/uploads/.empty 2> /dev/null
rm /home/box/web/public/css/.empty 2> /dev/null
rm /home/box/web/public/img/.empty 2> /dev/null
rm /home/box/web/public/js/.empty  2> /dev/null

# copy nginx configuration
ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
