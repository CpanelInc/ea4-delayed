# EA4 Delayed Production

## Target Audiences

1. Maintenance and security teams
2. Training and technical support
3. Managers and other internal key stakeholders
4. Future project/feature owners/maintainers

## Detailed Summary

Customer wanted to get EA4 updates days after production goes out in case there are problems found.

## Overall Intent

Allow servers to get new packages days after production is published.

## Options/Decisions

### Proper OBS project/Package Repository

1. require EA-RT to do the publish process for EA4-delayed X time after EA4-production
2. essentially take the same amount of resources (disk, BW, time, etc) as EA4-production
3. pkg only change
4. customers either install/remove the pkg as they see fit
5. force all consumers to the same delay
6. would work on all support cPanel's
7. would on affect EA4 pkgs
8. they could not manually update any packages until the the time window passes

### `tsunami` delayed-ea4 floodgate

1. keep the publishing simple
2. save another all the diskspace and bandwidth
3. require an ULC change to check the floodgate
4. require us to configure customers’ how they want it to be
5. allow us fine grained control (Customer X wants 2 days, Customer Y want 14 days, Customer Z wants these servers set to 1 day and these servers on 7 day)
6. require an updated ULC (which could be good to encourage upgrading)
7. would actually affect all packages not just EA4 (`pkgup`)
   * unless it would temporarily disable the EA4 repo while `pkgup` does what it does
8. they could manually update any pkg before the time window passes

### “light” Package Repository/Package

We could lighten the load of the Proper OBS project/Package Repository by:

* not be a real repo in the OBS-project sense
* make it just be a directory next to EA4-production that gets rsync’d 48 hours after the last publish to EA4-production
* the syncing would be a script/cmd that EA-RT runs at-will basically
   * cronned if we can programmatically determine when the last EA4-production push was
   * Called via any tools that do the publishing steps for us

### Repurpose OBS projects/Package Repositories

Instead of a new repo could we simply repurpose the public EA4 and EA4-production to be conceptually release and stable and just do the EA4-production dance X days after EA4.

Main draw back is everyone is already on production so a zillion people will suddenly be on the delayed schedule.

## Decision

Do: “light” Package Repository/Package

Why?

* reasonable amount of effort
* less resources
* does what customer is asking for
* `tsunami` floodgate would address a slightly different scenario, and we can/will do that later if needed
   * e.g. I have 10,000 srevers and I only want 1,000 per day to update

## Child Documents

None
