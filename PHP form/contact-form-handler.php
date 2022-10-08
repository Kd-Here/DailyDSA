<form action="" name="NameForm" method="post" role="form" autocomplete="" class="php-email-form">
              <div class="row">
                <div class="form-group col-md-6">
                  <label for="name">Your Name</label>
                  <input type="text" name="name" class="form-control" id="name" required>
                </div>
                <div class="form-group col-md-6">
                  <label for="name">Your Email</label>
                  <input type="email" class="form-control" name="email" id="email" required>
                </div>
              </div>
              <div class="form-group">
                <label for="name">Subject</label>
                <input type="text" class="form-control" name="number" id="subject" required>
              </div>
              <div class="form-group">
                <label for="name">Message</label>
                <textarea class="form-control" name="Message" rows="10" required></textarea>
              </div>
            </button>  

              <div class="text-center"><input style="background: #37b3ed"; name="submit" type="submit"></div>
            </form>
            <script>
              const scriptURL = 'https://script.google.com/macros/s/AKfycbz1MttA81GQWjXQP7EN_sDOx3dduFOeQMX1LbX7-ak7IwTwc8l_8nBR3v1OsFVlZxyUSQ/exec'
              const form = document.forms['NameForm']
            
            form.addEventListener('submit', e => {
              e.preventDefault()
              fetch(scriptURL, { method: 'POST', body: new FormData(form)})
              .then(response => alert("Thank you! your form is submitted successfully." ))
              .then(() => {  window.location.reload(); })
              .catch(error => console.error('Error!', error.message))
            })
          </script>