from django.core.management.base import BaseCommand, CommandError, no_translations
from polls.models import Question as Poll

class Command(BaseCommand):
  help = "Closes the specified poll for voting"

  def add_arguments(self, parser):
      # Positional arguments
      parser.add_argument("poll_ids", nargs="+", type=int)
      # Named (optional) arguments
      parser.add_argument(
        "--delete",  # Optional argument (flag)
        action="store_true",  # Sets options["delete"] to True if provided
        help="Delete poll instead of closing it",
    )
      
  @no_translations 
  def handle(self, *args, **options):
      for poll_id in options["poll_ids"]:
          try:
              poll = Poll.objects.get(pk=poll_id)
          except Poll.DoesNotExist:
              raise CommandError('Poll "%s" does not exist' % poll_id)

          '''poll.opened = False
          poll.save()

          self.stdout.write(
              self.style.SUCCESS('Successfully closed poll "%s"' % poll_id)
            )
          if options["delete"]:
            poll.delete()'''
          if options["delete"]:
                poll.delete()  # Delete the poll
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted poll "{poll_id}"'))
          else:
              poll.opened = False  # Close the poll
              poll.save()
              self.stdout.write(self.style.SUCCESS(f'Successfully closed poll "{poll_id}"'))
          verbosity = options["verbosity"]  # Get verbosity level
      if verbosity >= 2:
          self.stdout.write("Running the closepoll command with verbosity level:", verbosity)