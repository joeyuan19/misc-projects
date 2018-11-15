{
        smartInsert: function(elevator, floorNum) {
                                 if (elevator.destinationQueue.indexOf(floorNum) >= 0) {
                                                 console.log("nothing done");
                                                             return;
                                                                     }
                                         console.log(elevator.destinationQueue);
                                                 var above = floorNum > elevator.currentFloor();
                                                         if (elevator.goingUpIndicator()) {
                                                                         if (above) {
                                                                                             var i = 0;
                                                                                                             while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] < floorNum) {
                                                                                                                                     i++;
                                                                                                                                                     }
                                                                                                                             elevator.destinationQueue.splice(i,0,floorNum);
                                                                                                                                             elevator.checkDestinationQueue();
                                                                                                                                                         } else {
                                                                                                                                                                             var i = 1;
                                                                                                                                                                                             while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] > elevator.destinationQueue[i-1]) {
                                                                                                                                                                                                                     i++;
                                                                                                                                                                                                                                     }
                                                                                                                                                                                                             while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] > floorNum) {
                                                                                                                                                                                                                                     i++;
                                                                                                                                                                                                                                                     }
                                                                                                                                                                                                                             elevator.destinationQueue.splice(i,0,floorNum);
                                                                                                                                                                                                                                             elevator.checkDestinationQueue();
                                                                                                                                                                                                                                                         }
                                                                                 } else if (elevator.goingDownIndicator()) {
                                                                                                 if (above) {
                                                                                                                     var i = 1;
                                                                                                                                     while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] < elevator.destinationQueue[i-1]) {
                                                                                                                                                             i++;
                                                                                                                                                                             }
                                                                                                                                                     while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] > floorNum) {
                                                                                                                                                                             i++;
                                                                                                                                                                                             }
                                                                                                                                                                     elevator.destinationQueue.splice(i,0,floorNum);
                                                                                                                                                                                     elevator.checkDestinationQueue();
                                                                                                                                                                                                 } else {
                                                                                                                                                                                                                     var i = 0;
                                                                                                                                                                                                                                     while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] > floorNum) {
                                                                                                                                                                                                                                                             i++;
                                                                                                                                                                                                                                                                             }
                                                                                                                                                                                                                                                     elevator.destinationQueue.splice(i,0,floorNum);
                                                                                                                                                                                                                                                                     elevator.checkDestinationQueue();
                                                                                                                                                                                                                                                                                 }
                                                                                                         } else {
                                                                                                                         if (above) {
                                                                                                                                             elevator.goingUpIndicator(true);
                                                                                                                                                             elevator.goingDownIndicator(false);    
                                                                                                                                                                         } else {
                                                                                                                                                                                             elevator.goingUpIndicator(false);
                                                                                                                                                                                                             elevator.goingDownIndicator(true);
                                                                                                                                                                                                                         }
                                                                                                                                     elevator.goToFloor(floorNum);
                                                                                                                                             }
                                                                 console.log(elevator.destinationQueue);
                                                                     },
            init: function(elevators, floors) {
                              var shortcut = this.smartInsert;
                                      var e = elevators[0];
                                              e.on("idle", function(floorNum) {
                                                              e.goingUpIndicator(false);
                                                                          e.goingDownIndicator(false);
                                                                                  });
                                                      e.on("stopped_at_floor",function(floorNum) {
                                                                      if (floorNum > this.destinationQueue[0]) {
                                                                                          e.goingUpIndicator(false);
                                                                                                          e.goingDownIndicator(true);                
                                                                                                                      } else {
                                                                                                                                          e.goingUpIndicator(true);
                                                                                                                                                          e.goingDownIndicator(false);
                                                                                                                                                                      }
                                                                              });
                                                              for (var i = 0; i < floors.length; i++) {
                                                                              floors[i].on("up_button_pressed", function() {
                                                                                                  for (var j = 0; j < elevators.length; j++) {
                                                                                                                          shortcut(e,this.floorNum());
                                                                                                                                          }
                                                                                                              });
                                                                                          floors[i].on("down_button_pressed", function() {
                                                                                                              for (var j = 0; j < elevators.length; j++) {
                                                                                                                                      shortcut(e,this.floorNum());
                                                                                                                                                      }
                                                                                                                          });
                                                                                                  }
                                                                      e.on("floor_button_pressed",function(floorNum) {
                                                                                      shortcut(this,floorNum);
                                                                                              });
                                                                          },
                update: function(dt, elevators, floors) {
                                    // We normally don't need to do anything here
                                    //         console.log(elevators[0].destinationQueue);
                                    //             }
                                    //             }

{
    smartInsert: function(elevator, floorNum) {
        if (elevator.destinationQueue.indexOf(elevator) >= 0) {
            return;
        }
        var above = floorNum > elevator.currentFloor();
        if (elevator.goingUpIndicator()) {
            if (above) {
                var i = 0;
                while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] < floorNum) {
                    i++;
                }
                elevator.destinationQueue.splice(i,0,floorNum);
                elevator.checkDestinationQueue();
            } else {
                var i = 1;
                while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] > elevator.destinationQueue[i-1]) {
                    i++;
                }
                while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] > floorNum) {
                    i++;
                }
                elevator.destinationQueue.splice(i,0,floorNum);
                elevator.checkDestinationQueue();
            }
        } else if (elevator.goingDownIndicator()) {
            if (above) {
                var i = 1;
                while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] < elevator.destinationQueue[i-1]) {
                    i++;
                }
                while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] > floorNum) {
                    i++;
                }
                elevator.destinationQueue.splice(i,0,floorNum);
                elevator.checkDestinationQueue();
            } else {
                var i = 0;
                while (i < elevator.destinationQueue.length && elevator.destinationQueue[i] > floorNum) {
                    i++;
                }
                elevator.destinationQueue.splice(i,0,floorNum);
                elevator.checkDestinationQueue();
            }
        } else {
            if (above) {
                
                elevator.goingUpIndicator(true);
                elevator.goingDownIndicator(false);    
            } else {
                elevator.goingUpIndicator(false);
                elevator.goingDownIndicator(true);
            }
        }
    },
    init: function(elevators, floors) {
        var shortcut = this.smartInsert;
        var e = elevators[0];
        e.on("idle", function(floorNum) {
            e.goingUpIndicator(false);
            e.goingDownIndicator(false);
        });
        for (var i = 0; i < floors.length; i++) {
            floors[i].on("up_button_pressed down_button_pressed", function() {
                shortcut(e,this.floorNum());
            });
        }
        e.on("floor_button_pressed",function(floorNum) {
            shortcut(this,floorNum);
        });
    },
    update: function(dt, elevators, floors) {
        // We normally don't need to do anything here
    }
}
